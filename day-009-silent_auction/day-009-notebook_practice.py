#%% Dictionaries

programing_dictionaries = {
    "item1" : "value1",
    "item2" : "value2",
    "item3" : "value3",
    "item4" : "value4"
}

print(programing_dictionaries["item1"])
# adding to a dictionary
programing_dictionaries["item5"] = "value5"
print(programing_dictionaries)
#creating new dictinary
ned_dict = {}
#wipe out dictionary
# programing_dictionaries = {}
#editing
programing_dictionaries["item2"] = "edited"
print(programing_dictionaries)
#looping
for key in programing_dictionaries:
    print(key)

# %% Exercise 1 - Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():
    if value> 90:
        student_grades[key] = "Outstanding"
    elif value > 80 and value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif value > 70 and value <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

""" Alternate solution
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
"""

# 🚨 Don't change the code below 👇
print(student_grades)

# %% Exercise 2 - Dictionary in List
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

