######### DAY 4 #########
#%% Exercise 1 - Heads or Tails
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇
choice = ['Heads', 'Tails']
print(random.choice(choice))

#%% Exercise 2 - Banker Roulette
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(random.choice(list(names)))

#%% Exercise 2 - Banker Roulette - solution
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
random_selector = random.randint(0, num_items - 1)
payee = names[random_selector]
print(f"{payee} is going to buy the meal today!")

#%% Exercise 3 - Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

num_column = int(position[0]) -1
num_row = int(position[1]) -1
map[num_row][num_column] = "X"
# test cases
# print(f"column {num_column}")
# print(f"row {num_row}")
# print(type(num_column))
# print(type(num_row))
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


#%% Day 4 Project: Rock Paper Scissors

import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list_of_choices = [rock, paper, scissors]
while True:
          user_choice = input("'rock', 'paper', 'scissors': ")
          if user_choice == 'rock':
                    user_choice = rock
                    break
          elif user_choice == 'paper':
                    user_choice = paper
                    break
          elif user_choice == 'scissors':
                    user_choice = scissors
                    break
          else:
                    print("You mess up something, try again...")
                    continue

computer_choice = str(random.choice(list_of_choices))
print("You played: ")
print(user_choice)
print("Computer played: ")
print(computer_choice)

if user_choice == computer_choice:
          print("its a draw !")
elif user_choice == rock:
    if computer_choice == scissors:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == paper:
    if computer_choice == rock:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == scissors:
    if computer_choice == paper:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

# %%
