from calendar import c
from this import d
from tkinter import W
import random
guess = ""
result = ""
word_list = []
guessnum = 1
word_num = 0
word_file = open('names.txt','r')
for x in word_file:
    word_list.append(x)
print("Thank you for using the wordle bot. remember to type the guess you entered before you type the result. For entering the result, w - grey, y - yellow, g - green. I hope this helps you. Enjoy!")
while guessnum < 6:
   
    if guessnum == 1:
        print("Try salet.")
    elif guessnum == 2 and len(word_list) > 2:
        print("Try courd.")
    elif guessnum == 3 and len(word_list) > 5:
        print("Try nymph.")
    elif guessnum == 3 and len(word_list) <= 5:
        optimal_guess = random.choice(word_list)
        print("Try " + str(optimal_guess) + ".")
    elif guessnum >= 4:
        optimal_guess = random.choice(word_list)
        print("Try " + str(optimal_guess) + ".")
    
    guess = input("Guess: ")
    result = input("Result: ")
    word_list_tuple = tuple(word_list)
    if result == "ggggg":
       print("Solved with wordle_solver_v3.1 in " + str(guessnum) + " tries.")
       break
    for word in word_list_tuple:
        for x in range(5):
            if result[x] == "w" and guess[x] in word:
                 word_list.remove(word)
                 break
            elif result[x] == "y" and guess[x] in word[x]:
                word_list.remove(word)
                break
            elif result[x] == "y" and guess[x] not in word:
                word_list.remove(word)
                break
            elif result[x] == "g" and guess[x] not in word[x]:
                word_list.remove(word)
                break
    word_num = 0
    for x in word_list:
        word_num += 1
    
    
    if len(word_list) > 1:
        print("Possible words are:")
    if len(word_list) == 1:
        print("The word is: ")
    for x in word_list:
        print(x)
    guessnum += 1
    if word_num == 1:
        print
        print("Solved with wordle_solver_v3.1 in " + str(guessnum) + " tries.")
        break
    print(word_num)
    
    
