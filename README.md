# Hangman
Hangman is a guessing game for two or more players. One player thinks of a word,  and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.
In this project, computer randomly selects a word and a player tries to guess it.

## Playing Game
To quickly start a game,download and run final.py.This project has limited number of pre-loaded words. Don't peek at the list of words!

```
python final.py
```

## Project Details
The game is implemented as a Python class, Hangman that can be instantiated by passing in a list of potential words for the user to solve and the number of lives the user will have (essentially the number of incorrect guesses the user can have before losing the game). The Hangman class has the following attributes:

self.word - this is the word to be guessed and is generated upon instantiation by using the choice() method from the Python module random to randomly select one word from the list of words passed into the class

self.word_guessed - this is a representation of the word the user needs to guess, with underscores replacing any letters that have not been guessed yet. This list is printed at the beginning of the word, and after any guess.

self.num_letters - this is an integer representing the number of unique letters in the word still remaining to be guessed by the user

self.num_lives - this is an integer representing the number of remaining lives the user has in each instance of the game

self.word_list - a list of words (strings) from which the computer will randomly choose one for the user to guess

self.list_of_guesses - a list of all the letters that the user has tried during the game. This list is used to warn the user if a guess they enter has already been tried.

Hangman class has the following methods : 

ask_for_input(self): - This method takes input from the user and checks if input is single letter and alphabet.


check_guess(self) -  This method asks the user to guess a letter and  checks if the guess is in the word.

maskWord(self,state, word, guess) - This method is to mask and unmask the letters of the word to be guessed

Outside of the Hangman class definition, a function called play_game() is defined that accepts a list of possible words. Within this function definition, the number of lives are set and an instance of the Hangman class is created.

## Future Work 
In this project,computer randomly chooses a word to guess from the hard-coded list of words.In future, the game can be changed,  so that the user can load in their own lists of words. Another feature that can be added  to the game is to offer user the opportunity to get the clue.

