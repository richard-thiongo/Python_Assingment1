import random

# Choose a secret number between 1 and 100.
secret_number = random.randint(1, 100)

# Welcome the player and explain the game.
print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 100.")

# Keep asking for guesses until the player finds the secret number.
while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high! Guess again.")
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("Congratulations! You guessed the number!")
        break
