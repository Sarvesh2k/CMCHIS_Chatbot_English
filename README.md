# CMCHIS Chatbot

After two months of grinding, it's finally here! A chatbot that answers questions regarding the Tamil Nadu's Chief Minister's Comprehensive Health Insurance Scheme in English. The Natural Language Processing Toolkit (NLTK) was used for implementing the bot. And it also supports Whatsapp and Telegram integration!

## Introduction

Many people aren't aware of the schemes that have been launched by the Governemnt due to lack of information. As a result, people don't know how to access and apply to these schemes. The long queues in the Government Offices don't help either. How about we bring the scheme to the people, at the comfort of their homes? Thus comes the CMCHIS Chatbot. People can ask their queries to the chatbot and can be informed of the details and requirements to apply for the scheme. They can figure out the important keywords, and use the facilities effectively, reducing the burden on Government workers.

A retrieval based chatbot using NLTK, Keras, Tensorflow (Keras requires Tensorflow as a dependency) and Python were used to code the chatbot. A generative based chatbot wouldn’t be required in this scenario as the questions are domain specific and the users will only be asking questions mostly related to the scheme. The chatbot will be trained on the dataset which contains categories (intents), pattern and responses. A special recurrent neural network (LSTM) is used to classify which category the user’s message belongs to and then will give a random response from the list of responses.

## Software Requirements

- Python (3.6 or higher)
- NLTK Library
- NumPy
- Tensorflow and Keras (latest version preferred)
- Twilio
- Accounts on WhatsApp and Telegram

## How to Use the Code

In order to facilitate an in-depth understanding of how the code works and how to execute it, I have created a `Documentation.pdf` file that attempts to explain my exploration in this domain. Comments have also been provided in the codebase.

## Demonstration Video (Click to Watch)

[![CMCHIS Chatbot English](https://img.youtube.com/vi/TihtXnMT9E0/maxresdefault.jpg)](https://youtu.be/TihtXnMT9E0)

## Issues Faced during Development

1.	Named Entity Recognition (NER).
      1. It has to be said, the NER support in NLTK isn't that great.
      2. So, I tried exploring alternative to include the same. I looked into *SpaCy*, but it is a full-fledged framework, and I wanted a barebones model.
      2. With some digging around, I tried out the *StanfordNER Tagger*. It works pretty well, and I have included the code in the `Stanford_NER_Tagger.py` file. It is good to know some Java to delve into this library further.

2.	Cloud Hosting.
      1. The Tensorflow/Keras combination does require a lot of memory size. If you want to use free cloud providers like `Heroku`, you will run into memory issues.
      2. As a workaround, I tried downgrading the Tensorflow version to the point where it occupied less space, but it resulted into a lot of compile-time issues. Fortunately, I had Amazon Web Services to work with as part of my internship, and I didn't run into deployment issues there.

3.	WhatsApp integration.
      1. Unless you have a business account, you won't get access to the WhatsApp APIs.
      2. You can use the Twilio Sandbox for testing purposes, which is free and easy to work with.

## References
- Online Course: *Deep Learning Specialization offered by deeplearning.ai*
- [An appetizer for NLP](https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1) - If you want a gist of what NLP is.
- [Keras Documentation](https://keras.io/guides/)
- [NLTK Documentation](https://github.com/nltk/nltk/wiki)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Twilio Whatsapp API](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio) - Perfect for starting out WhatsApp integration
- [Telegram Bot APIs](https://core.telegram.org/bots/api) - Deploying a Chatbot in Telegram is fairly straightforward
- [Stanford NER](https://nlp.stanford.edu/software/CRF-NER.html) - The Java version
