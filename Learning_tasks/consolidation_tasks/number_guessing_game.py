# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# Define/assign number to a variable called magic_number

import random

magic_number = random.randint(1,100)
game_active = True
guesses = 5

# Ask user for input

print("you have five attempts to guess the magic number")

# Check if this input matches magic_number

while game_active:
    guess_number = int(input("enter a number: "))
    while guesses > 0:
        if guess_number == magic_number:
            print("you guessed the magic number")
            game_active = False
            guesses -= 1
        elif guess_number > magic_number:
            print("too high, guess again")
            guesses -= 1
        else:
            print("too low, guess again")
            guesses -= 1

# Let the user know if the response was correct or not


# Allow the user 5 guesses





