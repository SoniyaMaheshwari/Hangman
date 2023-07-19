from curses.ascii import isalpha
import random

def ask_for_input():
    if attempts > 0:
        guess = input('\n Enter a single letter:\t')
        guess = guess.lower()
        check_guess(guess)
    else:
        print("\n You exhausted your attempts, Sorry!")
        print(f" \n {word1.upper()} is the word")


def check_guess(guess):
    global guessed_letter
    global word
    global word1
    global attempts
    if (len(guess) == 1 and isalpha(guess)):

        
        if guess in guessed_letter:
            print("\n You already guessed this letter")
            #continue
            ask_for_input()
        else:

            if(guess in word):
                print(f"Good Guess! \t {guess} is in word")
                word = word.translate({ord(guess):None})
                
                if(len(word) == 0):
                    print(f"\nYou won the game! {word1.upper()} is the word")
                    #break
                guessed_letter += guess
                ask_for_input()

            else:
                print(f"\n Sorry, {guess} is not in the word. Try again." ) 
                attempts -= 1 
                guessed_letter += guess
                ask_for_input()
    else:
        print("\n Oops! That is not a valid input.")
        ask_for_input()

    
word_list = ["apple", "orange",'strawberry', 'peach', 'plum']
#print(word_list)
word = random.choice(word_list)
word1 = word
print(word)

guessed_letter = ''
print("You have 3 attempts to guess the word" )
attempts = 3
ask_for_input()

    