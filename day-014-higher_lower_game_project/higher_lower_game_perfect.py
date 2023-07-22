from game_data import data
import random
from art import logo, vs
from replit import clear

print(logo)

def random_item():
    return random.choice(data)

def format_choice(selected):
    """return string with name, desc and countyr, and return integer of followers"""
    return f"{selected['name']}, {selected['description']}, from {selected['country']}", selected['follower_count']

def user_choice():
    """check if user enter valid choice and return lower case selection"""
    while True:
        selected_mode = input("Who has more followers? Type 'A' or 'B': ").lower()
        if selected_mode == 'a' or selected_mode == "b":
            return selected_mode
        else:
            print("you mess it up, try again")

def brain(random_choice_a, random_choice_b, user_input):
    """compare number of followers and user choice, return True if user choose right and False if use choose wrong"""
    if random_choice_a > random_choice_b and user_input == 'a':
        return True
    elif random_choice_b > random_choice_a and user_input =='b':
        return True
    else:
        return False
# the same as: return (random_choice_a > random_choice_b and user_input == 'a') or (random_choice_b > random_choice_a and user_input == 'b')
# but let's not flame...

def check_duplicates(choice_a):
    choice_b, b_followers = format_choice(random_item())
    while choice_a == choice_b:
        choice_b, b_followers = format_choice(random_item())
    return choice_b, b_followers

def game():
    choice_a, a_followers = format_choice(random_item()) #assign to first variable display informations and number to second one number of followers
    print(choice_a)
#     print(a_followers) #test case
    choice_b, b_followers = check_duplicates(choice_a)
#     while a == b:
#         b, b_followers = format_choice(random_item())
    print(choice_b)
#     print(b_followers) #test case
    score_board = 0 # initial score is 0
    while brain(a_followers, b_followers, user_choice()) == True: #loop while user is on winning streak
        clear() # clear the screen
        print(logo) # display logo firs 
        score_board += 1 # increment score every time user guess correct anwser
        print(f"your score is: {score_board}")
        choice_a, a_followers = choice_b, b_followers # assign b valuse to a
        print(choice_a)
#         print(a_followers) # testing
        print(vs)
        choice_b, b_followers = check_duplicates(choice_a) # prevent random choice of the same items 
#         while a == b:
#             b, b_followers = format_choice(random_item())
        print(choice_b)
#         print(b_followers) # testing
    else:
        print(f"Wrong, your score is {score_board}")

game() #initialize the game
