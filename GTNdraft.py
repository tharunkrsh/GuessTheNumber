import numpy as np
import time

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

def rangeCheck(userNo, computerNo):
    if userNo < computerNo:
        print("Your guess is too low.")
        return False
    elif userNo > computerNo:
        print("Your guess is too high.")
        return False
    else:
        return True




def introGame():
    print("Welcome to Guess the Number!")
    time.sleep(1)
    print("In this game, you will try to guess the number I have selected.")
    time.sleep(1)
    print("You will be given a certain number of attempts based on the difficulty level you choose.")
    time.sleep(1)
    print("I will give you hints if your guess is too high or too low.")
    time.sleep(1)

difficulty = input("Please select a difficulty level (easy, medium, hard, extreme): ").lower()
# computer generates number based on difficulty level


computerNo = numbergen(difficulty)

if computerNo != False:
    ranges = {"easy": 5, "medium": 20, "hard": 50, "extreme": 100}
    guesses = {"easy": 3, "medium": 4, "hard": 5, "extreme": 6}
    print(f"I have selected a number between 1 and {ranges[difficulty]}.")
    time.sleep(1)
    print(f"Attempt to guess the number in {guesses[difficulty]} attempts.")
    time.sleep(1)
    print('I will tell you if your guess is too high or too low. Good luck!')

    time.sleep(1)

    guessCount = 0
    while guessCount < guesses[difficulty]:
        userNo = input("Please enter your guess: ")
        if not rangeCheck(int(userNo), computerNo):
            guessCount += 1
        else:
            print(f"Congratulations! You've guessed the number correctly in {guessCount + 1} attempts.")
            break
    
    if guessCount == guesses[difficulty]:
        print("Sorry, you've used all your attempts.")
    time.sleep(1)
    print(f"My number was {computerNo}.")

else:
        print("Invalid difficulty level selected. Please restart the game and choose a valid option.")