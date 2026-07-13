import numpy as np
import time

def introGame():
    print("Welcome to Guess the Number!")
    time.sleep(2)
    print("In this game, you will try to guess the number I have selected.")
    time.sleep(2)
    print("You will be given a certain number of attempts based on the difficulty level you choose.")
    time.sleep(2)
    print("I will give you hints if your guess is too high or too low.")
    time.sleep(2)

def get_difficulty():
    """Asks for difficulty until a valid one is entered."""
    options = ["easy", "medium", "hard", "extreme"]
    while True:
        difficulty = input("Please select a difficulty level (easy, medium, hard, extreme): ").lower()
        if difficulty in options:
            return difficulty
        print("Invalid difficulty level selected. Please try again.")

def numberGen(difficulty):
    if difficulty == "easy":
        return np.random.randint(1, 6)
    if difficulty == "medium":
        return np.random.randint(1, 21)
    if difficulty == "hard":
        return np.random.randint(1, 51)
    if difficulty == "extreme":
        return np.random.randint(1, 101)
    return False

introGame()
