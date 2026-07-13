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
    """Generates the computer's number based on
      the difficulty level."""
    
    #easy: 1-5, 3 guesses
    if difficulty == "easy":
        return np.random.randint(1, 6)
    
    #medium: 1-20, 4 guesses
    if difficulty == "medium":
        return np.random.randint(1, 21)
    
    #hard: 1-50, 5 guesses
    if difficulty == "hard":
        return np.random.randint(1, 51)
    
    #extreme: 1-100, 6 guesses
    if difficulty == "extreme":
        return np.random.randint(1, 101)
    
    return False

def rangeCheck(userNo, computerNo):
    if userNo < computerNo:
        print("Your guess is too low.")
        return False
    elif userNo > computerNo:
        print("Your guess is too high.")
        return False
    else:
        return True

def valid_guess(s):
    """error handling: returns True only if the string is a 
    whole number (no decimals, no letters)."""
    if len(s) == 0:
        return False
    for char in s:
        if char not in "0123456789":
            return False
    return True

def play_round(computerNo, max_guesses):
    """
    Runs one full round.
    Returns a tuple:
    (won (true/false), attempts_used)
    """

    guess_count = 0
    while guess_count < max_guesses:
        user_no = input("Please enter your guess: ")

        if not valid_guess(user_no):
            print("Please enter a valid whole number.")
            continue  # doesn't cost a guess

        if rangeCheck(int(user_no), computerNo):
            return True, guess_count + 1

        guess_count += 1

    return False, guess_count

def game():

    introGame()
    difficulty = get_difficulty()
    computerNo = numberGen(difficulty)
    
    ranges = {"easy": 5, "medium": 20, "hard": 50, "extreme": 100}
    max_guesses = {"easy": 3, "medium": 4, "hard": 5, "extreme": 6}







game()