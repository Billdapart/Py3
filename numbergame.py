#!/usr/bin/env python3

# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt
# appears again until the guess is correct, on successful guess, user will get a
# "Well guessed!" message, and the program will exit.

import random
n = random.randint(1, 9)
guess = int(input("Enter an integer from 1 to 9: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print ("Well guessed!")
        break
    print
