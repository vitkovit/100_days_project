# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = weight / (height)**2
# bmi_status = ["are underweight", "have a normal weight", "are slightly overweight", "are obese", "are clinically obese"]

# if bmi < 18.5:
#     status = 0
# elif 18.5 <= bmi < 25:
#     status = 1
# elif 25 <= bmi < 30:
#     status = 2
# elif 30 <= bmi < 35:
#     status = 3
# else:
#     status = 4
# print(f"Your bmi is {bmi:.1f}, you {bmi_status[status]}.")


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
print(str(score_true)+str(score_love))

