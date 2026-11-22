Mini Next-Token Predictor
# Project Description
This project is a simple educational statistical
language model designed to explore the fundamental concepts of language modeling and next-token prediction.
The model uses a Trigram approach, where two preceding words are used as context to predict
the next word.It provides a practical introduction to the basic ideas behind language
models and word-based prediction.
#1.Training Data
the model is trained using a small collection of
predefined English sentences.These sentences
provide the initial data from which the model
learns statistical relationships between words.
# 2.Tokenization
sentences are divided into individual words
using Pythons "split()" method.In this project
each word is treated as an individual token.
# 3.Model Training
The "train_model()" function processes the
training sentences and builds a
dictionary-based model.Each key consists of
two consecutive words, while its value contains
the possible next words observed in the training data.
This structure allows the model to associate a
two-word context with possible next-word predictions.
# 4.Context and Next-Token Prediction
The model uses two preceding words as 
context to predict the next word.This approach
is based on Trigram modeling which a
sequence consists of two context words and one predicted word.
# 5.Sentence Generation
The "generate_sentence()" function receives
two starting words from the user.These words
serve as the initial context for prediction.
The model selects a possible next word using
the available candidates in the training data.
The "random" module is used select among possible predictions.
As each new word is added the context is
updated allowing the model to attempt to
continue the sentence for up to five additional
words provided suitable predictions are available.
# 6.Main Function
the "main()" function connects model
training and sentence generation components.
It trains the model and displays the generated sentence.
The "if__name__ == "__main__":" statement
ensures that the main function runs when the Python file is executed directly.
# Technologies Used
Python
Dictionary data structure
Random module
Word-based tokenization
# Project Purpose
The purpose of this project is to gain a practical
understanding of language models
context-based prediction statistical
relationships between words and the
fundamental concept of next-token prediction.
This is a simple educational statistical model and
is not based on neural networks or Transformers
