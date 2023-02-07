######### DAY 4 #########
#%% Exercise 1 - Heads or Tails
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random
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

#%% Exercise 3 - Treasure Map

#%% Day 4 Project: Rock Paper Scissors