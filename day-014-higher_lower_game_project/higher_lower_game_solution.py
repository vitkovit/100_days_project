from game_data import data
import random
from art import logo, vs
from replit import clear



def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_anwser(guess, a_followers, b_folowers):
    if a_followers > b_folowers:
        return guess == 'a' # when evaluated it will return True, if it's b it will return False
    else:
        return guess == 'b'

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_anwser(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"you are right! CUrrent score is: {score}")
    else:
        game_should_continue = False
        print(f"you are wrong, final score is {score}")

# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds. 