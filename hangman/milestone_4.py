import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        pass

    def check_guess(self, guess):
        self.guess = guess.lower()
        if guess in self.word:
            print(f"Correct, {guess} is in {self.word}!")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
                else:
                    print(f"Sorry, {letter} is not in the word...")
                    self.num_lives -= 1
                    print(f"You have {self.num_lives} lives left")
                    


    def ask_for_input(self):
        while True:
            guess = str(input("Please make a guess"))
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'orange', 'pear']
    game = Hangman(word_list)
    game.ask_for_input()
