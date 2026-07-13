import numpy as np
import time

def introGame():
    print("Welcome to Guess the Number!")
    time.sleep(1)
    print("In this game, you will try to guess the number I have selected.")
    time.sleep(1)
    print("You will be given a certain number of attempts based on the difficulty level you choose.")
    time.sleep(1)
    print("I will give you hints if your guess is too high or too low.")
    time.sleep(1)

def numbergen(difficulty):
    if difficulty == "easy":
        return np.random.randint(1, 6)
    if difficulty == "medium":
        return np.random.randint(1, 21)
    if difficulty == "hard":
        return np.random.randint(1, 51)
    if difficulty == "extreme":
        return np.random.randint(1, 101)
    return False