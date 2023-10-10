######### DAY 3 #########
#%% Exercise 1 - Odd or Even
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number%2 == 1:
    print("This is an odd number")

else:
    print("This is an even number.")

#%% Exercise 2 - BMI 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height)**2
bmi_status = ["are underweight", "have a normal weight", "are slightly overweight", "are obese", "are clinically obese"]

if bmi < 18.5:
    status = 0
elif 18.5 <= bmi < 25:
    status = 1
elif 25 <= bmi < 30:
    status = 2
elif 30 <= bmi < 35:
    status = 3
else:
    status = 4
print(f"Your bmi is {bmi:.1f}, you {bmi_status[status]}.")

#%% Exercise 2 - BMI 2.0 solution
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height)**2
bmi_status = ["are underweight", "have a normal weight", "are slightly overweight", "are obese", "are clinically obese"]

if bmi < 18.5: 
    status = 0
elif 18.5 <= bmi < 25:
    status = 1
elif 25 <= bmi < 30:
    status = 2
elif 30 <= bmi < 35:
    status = 3
else:
    status = 4
print(f"Your BMI is {bmi:.0f}, you {bmi_status[status]}.")


#%% Exercise 3 - Leap Year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#%% Exercise 4 - Pizza Order Practice
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25

if add_pepperoni == "Y":
    if size == "M" or size == "L":
        price = price +3
    else:
        price += 2

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")

#%% Exercise 5 - Love Calculator

#🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
condition_true = ["t","r","u","e"]
condition_love = ["l","o","v","e"]

score_true = 0
score_love = 0
combined = name1.lower() + name2.lower()

for i in combined:
   #print(i)
    for k in condition_true:
        if i == k:
          #print(k)
          score_true += 1

for i in combined:
   #print(i)
    for k in condition_love:
        if i == k:
          #print(k)
          score_love += 1
total_score = str(score_true)+str(score_love)
# print(str(score_true)+str(score_love))

total_score_int = int(total_score)
# print(type(total_score))
# print(type(total_score_int))

if (total_score_int < 10) or (total_score_int > 90):
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score_int >= 40) and (total_score_int <= 50):
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")


# %% Exercise 5 - Love Calculator solution

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

#%% Day 3 Project: Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# https://www.asciiart.eu/
# https://ascii.co.uk/

#Write your code below this line 👇

direction = input("left or right? ").lower()

if direction == "left" or direction == "r":
          print("you choose to go left, goooood")
          action = input("swim or wait? ").lower()
          if action == "wait":
                    print("you choose to wait, goooood")
                    choice = input("Which door, Yellow, Blue or Red? ").lower()
                    if choice == "yellow" or choice == "y":
                              print("You Win, this time....")
                    elif choice == "red" or choice == "r":
                              print("Burned by fire. Game Over.")
                    elif choice == "blue" or choice == "b":
                              print("Eaten by beasts. Game Over.")
                    else:
                              print("Game Over Loser!.")
          else:
                    print("Attacked by trout. Game Over.")

else:
          print("Fall into a hole. Game Over.")



# %%
