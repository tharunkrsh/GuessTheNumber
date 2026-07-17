import numpy as np
import time
import sys

# global variables to track statistics
wins = 0
losses = 0
games_played = 0
win_rate = 0
avg_accuracy = 0
total_accuracy = 0

def typewriter(text, delay=0.035):
    """Prints text one character at a time like a typewriter."""

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to a new line once the full line is typed out

def intro_game():
    """Function prints the introduction to the game."""
    banner = r"""
   _____ _    _ ______  _____ _____    _______ _    _ ______ 
  / ____| |  | |  ____|/ ____/ ____|  |__   __| |  | |  ____|
 | |  __| |  | | |__  | (___| (___       | |  | |__| | |__   
 | | |_ | |  | |  __|  \___ \\___ \      | |  | |__| | __|  
 | |__| | |__| | |____ ____) |___) |     | |  | |  | | |____ 
  \_____|\____/|______|_____/_____/      |_|  |_|  |_|______|
             _   _ _   _ __  __ ____  _____ ____  
            | \ | | | | |  \/  | __ )| ____|  _ \ 
            |  \| | | | | |\/| |  _ \|  _| | |_) |
            | |\  | |_| | |  | | |_) | |___|  _ < 
            |_| \_|\___/|_|  |_|____/|_____|_| \_\
    """
    print(banner)
    time.sleep(1.5)
    typewriter("Welcome to Guess the Number!")
    time.sleep(1)
    typewriter("In this game, you will try to guess the number I have selected.")
    time.sleep(1)
    typewriter("You will be given a certain number of attempts based on the difficulty level you choose.")
    time.sleep(1)
    typewriter("I will give you hints if your guess is too high or too low.")
    time.sleep(1)

def get_difficulty():
    """Returns a valid difficulty level selected by the user."""

    options = ["easy", "medium", "hard", "extreme"]
    # loop until user enters a valid difficulty
    while True:
        difficulty = input("Please select a difficulty level (easy, medium, hard, extreme): ").lower()
        if difficulty in options:
            return difficulty
        typewriter("Invalid difficulty level selected. Please try again.")

def number_gen(difficulty):
    """Returns the computer's number 
    based on the difficulty level 
    (Random number generator)."""
    
    #easy: 1-5, 3 guesses
    if difficulty == "easy":
        return np.random.randint(1, 6)
    
    #medium: 1-15, 4 guesses
    if difficulty == "medium":
        return np.random.randint(1, 16)
    
    #hard: 1-50, 5 guesses
    if difficulty == "hard":
        return np.random.randint(1, 51)
    
    #extreme: 1-100, 6 guesses
    if difficulty == "extreme":
        return np.random.randint(1, 101)
    
    return False

def WIN_check(user_no, computer_no):
    """Returns True if the guess is correct
    and False otherwise. 
    Also prints hints if the guess is too high 
    or too low."""

    if user_no < computer_no:
        print("Your guess is too low.")
        return False
    
    elif user_no > computer_no:
        print("Your guess is too high.")
        return False
    
    else:
        # user guessed correctly
        return True

def valid_guess(s):
    """error handling: 
    checks if the user's guess is a valid whole number."""
    # returns True only if the string is a 
    # whole number (no decimals, no letters).

    if len(s) == 0:
        return False
    for char in s:
        if char not in "0123456789":
            return False
    return True

def in_range(user_no, ranges):
    """error handling:
    checks if the user's guess is within the valid range."""
    # if guess is in range, return True, else return False

    return 1 <= user_no <= ranges

def play_round(computer_no, max_guesses, max_range):
    #inputs: computer's guess, max number of guesses,
    # upper bound of difficulty level.
    """
    Runs one full round.
    Returns a tuple:
    (won, attempts_used, accuracy)
    
    won: True if the user guessed correctly, False otherwise.
    attempts_used: the number of guesses the user made.
    accuracy: how quickly the user guessed the number
    (lower the guesses, higher the accuracy).
    """

    # intro based on difficulty
    typewriter(f"I have selected a number between 1 and {max_range}.")
    time.sleep(1)
    typewriter(f"Attempt to guess the number in {max_guesses} attempts.")

    guess_count = 0
    # loop until the user has used all their guesses
    while guess_count < max_guesses:
        user_no = input("Please enter your guess: ")

        # error handling for invalid input
        if not valid_guess(user_no):
            typewriter("Please enter a valid whole number.")
            continue  # doesn't cost a guess
        
        # error handling for out of range input
        if not in_range(int(user_no), max_range):
            typewriter(f"Please enter a number between 1 and {max_range}.")
            continue # doesn't cost a guess
        
        # checks if user has won 
        if WIN_check(int(user_no), computer_no):
            # game is won, return True, number of guesses used, accuracy
            return True, guess_count + 1, ((max_guesses - guess_count)/max_guesses) *100
        
        guess_count += 1

    #game is lost, return False, number of guesses used, and accuracy
    return False, guess_count, 0

def play_again():
    """Asks the user if they want to play again."""

    # loops until the user enters a valid response (y/n).
    while True:
        response = input("Do you want to play again? (y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            typewriter("Great guessing with you! See you next time.")
            return False
        else:
            typewriter("Invalid input. Please enter 'y' or 'n'.")

def game():
    """Main function to run the game, all other functions are called from here."""

    # track statistics across one 'session' of the game (until user decides to stop replaying).
    global wins, losses, games_played, win_rate, avg_accuracy, total_accuracy
    
    # call the intro function to print the introduction to the game
    intro_game()

    # define the upper bound and max guesses for each difficulty
    ranges = {"easy": 5, "medium": 15, "hard": 50, "extreme": 100}
    max_guesses = {"easy": 3, "medium": 4, "hard": 5, "extreme": 6}

    # loop until the user decides to stop playing
    while True:
        # ask user for difficulty level and generate the computer's number
        difficulty = get_difficulty()
        computer_no = number_gen(difficulty)

        # play one round of the game, and retrieve the results
        # play_round() function docstring gives details on what is returned
        won, attempts, accuracy = play_round(computer_no, max_guesses[difficulty], ranges[difficulty])
        
        # displays message and round statistics
        if won:
            typewriter(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
            time.sleep(1)
            typewriter(f"Your accuracy was {accuracy:.2f}%.")

            # adds to the total wins and accuracy for the session
            wins += 1
            total_accuracy += accuracy

        else:
            typewriter(f"Sorry, you've used all your attempts. The correct number was: {computer_no}")
            time.sleep(1)
            typewriter(f"Your accuracy was {accuracy:.2f}%.")

            # adds to the total losses and accuracy for the session
            # (accuracy is 0 for a loss)
            losses += 1
            total_accuracy += accuracy
        
        # updates total session statistics
        games_played = wins + losses

        if games_played > 0:
            # calculates win rate
            win_rate = (wins / games_played) * 100
            # calculates average accuracy across games
            avg_accuracy = total_accuracy / games_played
        
        else:
            win_rate = 0
            avg_accuracy = 0

        if input("Do you want to see your stats?: ").lower() in ("y", "yes"):
            typewriter("\n--- Your Stats ---")
            typewriter(f"Games played:      {games_played}")
            typewriter(f"Wins:              {wins}")
            typewriter(f"Win rate:          {win_rate:.2f}%")
            typewriter(f"Average accuracy:  {avg_accuracy:.2f}%")
            typewriter("------------------\n")

        # prompts the user to play again/stop playing
        if not play_again():
            break
    
    typewriter("\n--- Final Stats ---")
    typewriter(f"Games played:      {games_played}")
    typewriter(f"Wins:              {wins}")
    typewriter(f"Win rate:          {win_rate:.2f}%")
    typewriter(f"Average accuracy:  {avg_accuracy:.2f}%")
    typewriter("-------------------\n")

game()