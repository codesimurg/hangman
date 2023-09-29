
import random
class Hangman:
    
    
    
    def __init__(self, word_list, num_lives = 5):
        
        self.word_list = word_list
        #The number of lives the player has at the start of the game.
        self.num_lives = num_lives
        #The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
        self.word = random.choice(self.word_list)
        #A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.word_guessed =["_"] * len(self.word)
        #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))
        #A list of words
        self.word_list = None
        #A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []

    
    def check_guess(self, guess):
        self.guess = self.guess.lower()
        
        if self.guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        for index, letter in enumerate(self.word):
            if letter == self.guess:
                self.word_guessed[index] = self.guess
                self.word_guessed = "".join(self.word_guessed)
            else:
                self.num_lives = self.num_lives - 1
                print(f"Sorry, {self.guess} not in the word.")
                print(f"You have {self.num_lives} lives left.")
        self.num_letters = self.num_letters - 1
            
    def ask_for_input(self):
        while True:
            self.guess = input("Please enter a single letter: ")
            
            if len(self.guess) != 1 or not self.guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)
    