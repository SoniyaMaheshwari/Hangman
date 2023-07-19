from curses.ascii import isalpha
import random
word_list = ["apple", "orange",'strawberry', 'peach', 'plum']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input('Enter a single letter:\t')
if (len(guess) == 1 and isalpha(guess)):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
