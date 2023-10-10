############DEBUGGING#####################

#%%
# Describe Problem
def my_function():
  for i in range(1, 20): #changing 20 to 21
    if i == 20:
      print("You got it")
my_function()

#%%
# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # from 0 to 5
print(dice_imgs[dice_num])

#%%
# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:   # turn > to >=
  print("You are a Gen Z.")

#%%
# Fix the Errors
age = int(input("How old are you?")) #convert to int
if age > 18:
    print(f"You can drive at age {age}.") #inser f string

#%%
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # should not be ==
total_words = pages * word_per_page
print(total_words)

#%% 
#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # add 2 more spaces
  print(b_list)

mutate([1,2,3,5,8,13])
# %%
