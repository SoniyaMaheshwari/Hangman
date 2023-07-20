# Hangman
Hangman is a guessing game for two or more players. One player thinks of a word,  and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.
In this project, computer randomly selects a word and a player tries to guess it.

## Milestone1
Here, I have used python language to implement this game.

## Milestone2

Here I have created two functions.
1)ask_for_input() function: It takes a single alphabet as input from the user
2)check_guess() function: It checks if the letter is in the word.
User is given 5 attempts to guess the correct word.

## Milestone3

Here I have created a class called Hangman
a) It has following attributes
* num_lives: number of attempts user can have
* word_list: list of words from which computer randomly selects the word
* num_letters: List of all letters from which a user can select a alphabet
* state: This attribute is used to mask the letters of the word

b) It has following methods
* ask_for_input() method
* check_guess() method
* maskWord() method: It is used to unmask the letters from the word as user guesses them.

