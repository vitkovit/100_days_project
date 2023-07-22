from art import logo
from random import randint

print(logo)
print("You just need to guess number between 1 and 100")

random_number = randint(1, 100)
random_increment = randint(1, 5)
random_decrement = randint(1, 5)

def user_select():
    while True:
        selected_mode = input("Select difficulty 'easy' or 'hard': ").lower()
        if selected_mode == 'easy':
            return 5
        elif selected_mode == 'hard':
            return 10
        else:
            print("you mess it up, try again")

def check_input():
    while True:
        user_guess_input = input("Guess a number: ")
        try:
            user_guess_input = int(user_guess_input)
            return int(user_guess_input)
        except ValueError:
          print("That's not an integer. Please try again.")
        
def check_awnser(user_guess_input, guess_attempt):
        if user_guess_input > random_number:
            print("too high")
            return guess_attempt - 1
        elif user_guess_input < random_number:
            print("too low")
            return guess_attempt - 1
        else:
            print(f"{user_guess_input} is correct!")
            
def game_play():
     guess_attempt = user_select()
     while guess_attempt != random_number:
        user_guess_input = check_input()
        guess_attempt = check_awnser(user_guess_input, guess_attempt)
        if guess_attempt is not None and guess_attempt <= 3:
            print(f"number should be between {random_number - random_decrement} and {random_number + random_increment}")
        if guess_attempt == 0:
            print("sorry you run out of moves")
            print(f"number was: {random_number}")
            break

game_play()
    

