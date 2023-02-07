######### DAY 1 #########

#%% Exercise 1 - Printing
#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#%% Exercise 2 - Debugging Practice

#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


#%% Exercise 3 - Input Function

#Write your code below this line 👇

print(len(input("What is your name? ")))


#%% Exercise 4 - Variables

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp = a
a= b
b = temp

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#%% Day 1 Project: Band Name Generator
#Go to: https://replit.com/@appbrewery/band-name-generator-start?v=1
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
