# coding: utf-8

import nltk
from nltk.tag.stanford import StanfordNERTagger

import os
java_path = "C:/Program Files/Java/jdk-11.0.1/bin/java.exe"
os.environ['JAVAHOME'] = java_path

sentence = u"Twenty miles east of Ram, Nev., " \
    "where packs of wild mustangs roam free through " \
    "the parched landscape, Tesla Gigafactory 1 " \
    "sprawls near Interstate 80." \
    "His name is Elon Musk, a visionary."

jar = 'C:/Users/lenovo/Desktop/Chatbot/cmch-bot/Lib/stanford-ner/stanford-ner.jar'
model = 'C:/Users/lenovo/Desktop/Chatbot/cmch-bot/Lib/stanford-ner/english.all.3class.distsim.crf.ser.gz'

def custom_validate_fullname(words):
    tags = ner_tagger.tag(words)
    tag_string = ""
    for tag in tags:
        if tag[1] == "PERSON":
            tag_string += str(tag[0]) + " "
    return tag_string if tag_string != "" else None

# Prepare NER tagger with english model
ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

# Tokenize: Split sentence into words
words = nltk.word_tokenize(sentence)
ptag = custom_validate_fullname(words)

# Run NER tagger on words
print(ner_tagger.tag(words))
print("You are talking about " + ptag)

