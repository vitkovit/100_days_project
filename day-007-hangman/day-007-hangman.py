#%% Hangman epositioncersize attempt 
import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear
world_list = ['heads', 'tails', 'frog', 'bat', 'apple']
random_word = random.choice(word_list)

print(logo)

guess_letter = ""           # placeholder for user input 
end_of_geme = False         # boolean check of gamse status
lives = 6                   # lives based on hangman_art stages
listed_word = []            #will create list from random word
letter_placeholder = []     #will create lenght of dashes based on lengt of a word 

for letter in random_word:
    listed_word.append(letter)
 
for _ in range(len(random_word)):
    letter_placeholder += "_"

# print(listed_word)
# print(letter_placeholder)

while not end_of_geme:
    guess_letter = input("Guess the letter: ").lower()
    clear()                 # clear screen after input
    for position in range(len(listed_word)):
        if listed_word[position] == guess_letter:
            letter_placeholder[position] = guess_letter
    if guess_letter not in listed_word: # check if input is in the random word (list)
        lives -= 1 

    print(' '.join(letter_placeholder))
    if "_" not in letter_placeholder:
        end_of_geme = True
        print("you win")
    
    if lives == 0:
        print("you are a looser!")
        end_of_geme = True
    print(stages[lives])
