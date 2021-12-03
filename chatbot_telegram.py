from threading import Timer
from twilio.twiml.messaging_response import MessagingResponse
import requests
from flask import Flask, request
import random
import json
from keras.models import load_model
import numpy as np
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from bottle import (
    run, post, response, request as bottle_request
)    

model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - splitting words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stemming every word - reducing to base form
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for words that exist in sentence
def bag_of_words(sentence, words, show_details=True):
    # tokenizing patterns
    sentence_words = clean_up_sentence(sentence)
    # bag of words - vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % word)
    return(np.array(bag))


def predict_class(sentence):
    # filter below  threshold predictions
    p = bag_of_words(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result


# Telegram Messaging Sandbox

BOT_URL = 'https://api.telegram.org/bot1278289981:AAFVVidHTaUY1Vy764247BMFm2O1uGS2UTU/' # <--- add your telegram token here
def get_chat_id(data):  
    """
    Method to extract chat id from telegram request.
    """
    chat_id = data['message']['chat']['id']
    return chat_id
    
def get_message(data):  
    """
    Method to extract message from telegram request.
    """
    message_text = data['message']['text']
    return message_text
    
def send_message(prepared_data):  
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """ 
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, data=prepared_data)  # don't forget to make import requests lib

def prepare_data_for_answer(data):  
    
    ints = predict_class(get_message(data))
    res = getResponse(ints, intents)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(res)
    
    json_data = {
        "chat_id": get_chat_id(data),
        "text": str(res),
    }
    return json_data
    
def timeout():
    json_data = {
        "chat_id": get_chat_id(data),
        "text": "Are you there?"
    }
    send_message(json_data)
    
@post('/')

def main():  
    global data 
    data = bottle_request.json
    answer_data = prepare_data_for_answer(data)
    send_message(answer_data)  # <--- function for sending answer
    t= Timer(20, timeout)
    print("Timer Started!")
    t.start()
    return response  # status 200 OK by default
if __name__ == '__main__':  
    run(host='localhost', port=8080, debug=True)
