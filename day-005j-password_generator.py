######### DAY 5 #########
#%% Exercise 1 - Average Height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  intstudent_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

#   total_heights = 0
#   for heights in student_heights:
#     total_heights += int(heights)  
# average = round(total_heights / (n + 1))
# print(average)

#%% Exercise 2 - High Score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highes_score = 0
for score in student_scores:
    if score > highes_score:
      highes_score = score
print(f"The highest score in the class is: {highes_score}")

#%% Exercise 3 - Adding Even Numbers
total = 0
for number in range (1, 101):
  total += number
print(total)

total = 0
for number in range (2, 101, 2):
  total += number
print(total)

#%% Exercise 4 - FizzBuzz
#Write your code below this row 👇
total = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print(number)

#%% Day 5 Project: Create a Password Generator
#Password Generator Project
# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

master_list = []
for letter in range (0, nr_letters):
    random_letters = random.choice(letters)
    master_list.append(random_letters)

for number in range (0, nr_numbers):
    random_numbers = random.choice(numbers)
    master_list.append(random_numbers)

for symbol in range (0, nr_symbols):
    random_symbols = random.choice(symbols)
    master_list.append(random_symbols)

# unshuffeled list 
print(master_list)
random.shuffle(master_list)
# list after shuffle  
print(master_list)
password = "".join(master_list)
print(f"here is your password: {password}")


# %%
