#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

print(logo)
print("You just need to guess number between 1 and 100")

random_number = randint(1, 100)
random_increment = randint(1, 5)
random_decrement = randint(1, 5)


while True:
    selected_mode = input("Select difficulty 'easy' or 'hard': ").lower()
    if selected_mode == 'easy' or selected_mode == 'hard':
        break
 
if selected_mode == 'easy':
    number_of_guesses = 10
else:
    number_of_guesses = 5
guess_attempt = 0
while guess_attempt <= number_of_guesses:
    user_guess = int(input("Guess a number: "))
    if user_guess > random_number:
        print("too high")
    elif user_guess < random_number:
        print("too low")
    else:
        print("that is correct!")
        break
    guess_attempt += 1
    guess_remains = number_of_guesses - guess_attempt
    if guess_remains <= 3:
        print(f"number should be between {random_number - random_decrement} and {random_number + random_increment}")
    if guess_remains == 0:
        print("sorry you run out of moves")
        print(f"number was: {random_number}")

        break
    print(f"you have {guess_remains} attempts remaining")




    

