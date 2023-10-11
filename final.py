
from curses.ascii import isalpha
import random
import string

class Hangman: 
    def __init__(self,word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list) # this is to randomly choose a letter from word_list
        self.word1 = self.word
        self.word_guessed = []
        self.num_letters = list(string.ascii_uppercase) # this contains the list of all letters
        self.list_of_guesses = []
        self.state = "_" * len(self.word) # mask the word
        #self.ask_for_input()
        print("You have 5 lives")
    

    
    def ask_for_input(self):
        '''
         #This method asks for input from the user and checks if the input is a single letter and a alphabet
        '''
        
        while True:
            if self.num_lives: # check if user has exhausted all his attempts
                #print("*******************************************************")
                print(f"\n\n{self.state}\n")
                print(f"Guess letters from \t {self.num_letters}")
                self.guess= input("\nEnter a single letter \t ").lower()
                
                #self.guess=self.guess.lower()
                if (len(self.guess) == 1 and isalpha(self.guess)):
                    if self.guess in self.list_of_guesses:
                        print("\n You already guessed this letter")
                        continue
                    else:
                        print(self.guess)
                        self.list_of_guesses.append(self.guess)
                        self.num_letters.remove(self.guess.upper())
                        self.check_guess()
                        
                else:
                    print("\n Oops! That is not a valid input.") # This statement is executed when the user enter incorrect input
                    continue
            else:
                print("\n Sorry!, You Lost\n")
                break #want to know why break statement is not working here, Moderator please explain.
            return
              
                
    def check_guess(self):
        '''
        This method checks if the user has correctly guessed the letter  
        '''
        if(self.guess in self.word): 
            print(f"\nGood Guess! \t {self.guess} is in word")
            self.word = self.word.translate({ord(self.guess):None})
            self.state =self.maskWord(self.state,self.word1,self.guess)
            
            
            if(len(self.word) == 0):
                print(f"\n Congratulations !!! You won the game! {self.word1.upper()} is the word\n")
                return
                
            self.ask_for_input()

        else:
            print(f"\n Sorry, {self.guess} is not in the word. Try again." ) 
            self.num_lives -= 1 
            print(f"\n You have {self.num_lives} lives left")
            self.ask_for_input()


    def maskWord(self,state, word, guess):
        '''
          This method is to mask and unmask the letters of the word to be guessed
        '''
        state = list(state)
        for i in range(len(word)):
            if word[i] == guess:
                state[i] = guess.upper()
        return "".join(state)


def play_game(word_list):
    num_lives = 5
    player1 = Hangman(word_list,num_lives)
    player1.ask_for_input()
    

if __name__ == "__main__":
    word_list = ["apple", "orange",'strawberry', 'peach', 'plum']
    play_game(word_list)

        



