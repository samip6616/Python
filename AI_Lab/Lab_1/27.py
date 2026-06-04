import random  # Used to generate a random number

# Function to run the guessing game
def guessing_game():
    number = random.randint(1, 100)  # Random number between 1 and 100
    max_attempts = 7                 # Maximum number of guesses allowed
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("You have 7 attempts to guess the number between 1 and 100.")

    # Loop until attempts run out or correct guess
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Attempts left:", max_attempts - attempts)
        elif guess > number:
            print("Too high! Attempts left:", max_attempts - attempts)
        else:
            print("Congratulations! You guessed the number.")
            print("Total attempts used:", attempts)
            return  # End the function

    # If user fails within 7 attempts
    print("Sorry! You've used all attempts.")
    print("The correct number was:", number)


# Start the game
guessing_game()