#%%
def greet():
    print("something")

greet()
# %%
def greet_with(name, location):
    print(f"hello {name}, how is in {location}?")
greet_with('Tom', 'hell')

greet_with(location='Moon', name='Neil')

# %% Exercise 1 - Paint Area Calculator

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    num_of_cans = math.ceil((test_h * test_w) / coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#%% Exercise 2 - Prime Numbers 

#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#%% Caesar Cipherv 01

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
 
def enript(plain_text, shift_amount):
    chiper_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        chiper_text = chiper_text + alphabet[new_position]
    print(f"the encoded text is {chiper_text}")

def decript(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text = plain_text + alphabet[new_position]
    print(f"the decoded text is {plain_text}")

if direction == "encode":
    enript(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decript(cipher_text=text, shift_amount=shift)



#%% Caesar Cipherv 02
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesary(start_txt, shift_amount, cipher_direction):
    end_text = ""
    # we need to move this out of for loop
    if cipher_direction == "decode":
        shift_amount = shift_amount * -1
    for letter in start_txt:
        position = alphabet.index(letter)
        # if cipher_direction == "decode":
        #     shift_amount = shift_amount * -1
            # because 5 * -1 = -5
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}" )
    #this was a bug

caesary(start_txt=text, shift_amount=shift, cipher_direction=direction)




#%% Caesar Cipher v03
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_txt, shift_amount, cipher_direction):
    end_text = ""
    # we need to move this out of for loop
    if cipher_direction == "decode":
        shift_amount = shift_amount * -1
    for char in start_txt:
        #position = alphabet.index(char)
        # if cipher_direction == "decode":
        #     shift_amount = shift_amount * -1
            # because 5 * -1 = -5
        if char in alphabet: # only if input is in aplhabet
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}" )
    #this was a bug
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # this will let you fit whatever user enter in to 26
    caesar(start_txt=text, shift_amount=shift, cipher_direction=direction)

    check_end = input("do you want to continue? (yes or no): ")

    if check_end == "no":
        should_end = True
        print("bye..")

# %%
