import random

word_list = ["banana", "pomegranate", "grapefruit", "clementine", "blueberry"]
word = random.choice(word_list)
print(word)

def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
