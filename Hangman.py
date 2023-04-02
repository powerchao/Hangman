import requests
import random

# defines site to access
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

# sends request to defined site and obtains entire response in one variable
response = requests.get(word_site)
# splits response content into list of values
WORDS = response.content.splitlines()
# selects a random word from the list and converts it into a string
target_word = str(random.choice(WORDS))
# slices off the b' and trailing ' that seems to come with every target_word generation
target_word = target_word[2:len(target_word)-1]
# ensures min length of target word
while len(target_word) < 6:
    target_word = str(random.choice(WORDS))
    target_word = target_word[2:len(target_word)-1]
# defining empty list variables
underscore_list = []
guessed_letter_list = []
# filling the obscured list with a quantity of underscores equal to the length of the targer word
for number in range(0,len(target_word)):
    underscore_list += "_"
# setting max lives
player_lives = 7

# generates a presentable string from the obscured word list
def generate_clue():
    underscore_string = ""
    for number in range(len(target_word)):
        underscore_string += underscore_list[number]
    return underscore_string

# generates a presentable string from the guessed letters list
def generate_guessed_letters():
    generated_answer = "Guessed letters: "
    for letter in guessed_letter_list:
        generated_answer += letter + " "
    return generated_answer

# This is the beginning of the playing sequence. While any letters remain unguessed and the player has guesses remaining, loops through the turns.
# The player is given their remaining lives, the obscured clue word, and their guessed letters. They are then asked to guess a letter. 
# User input is put into lowercase, then assessed for containing non-letters or being any longer than one length. If it fails this check, returns to guess without deducting life.
# Checks if letter was already guessed. If guessed, does not deduct a life and requests another input. If not guessed, adds to list of guessed letters and begins checks.
# While checking letter, defines a boolean and crawls through the target word, comparing each indexed letter with the player input. 
# Boolean is toggled to True if player input matches any letter of target word.
# If boolean remains false after the crawling of the letters, deduct a life and inform player of missed guess.
# If boolean is true, re-crawl through target word but using an integer range, and replacing the underscores in our underscore list with the players guessed
# letter as the range of the target word string and underscore list will always be identical. The list is referenced at the correct index only when the matches occur.
# Then the turn begins again from the beginning of this comment section.

while generate_clue() != target_word and player_lives > 0:
    print(f"You have {player_lives} missed guesses remaining.")
    print(generate_clue())
    print(generate_guessed_letters() + "\n")
    guessed_letter = input("Which letter are you guessing?\n").lower()
    if not guessed_letter.isalpha() or len(guessed_letter)!=1:
        print("That input is not valid, please enter a single letter with no punctuation or symbols.\n")
    elif guessed_letter not in guessed_letter_list:
        guessed_letter_list += guessed_letter
        matches_word = False
        for character in target_word:
            if guessed_letter == character:
                matches_word = True
        if matches_word == False:
            player_lives -= 1
            print(f"The letter {guessed_letter} is not in the word.\n")
        else:
            for number in range(len(target_word)):
                if  guessed_letter == target_word[number]:
                    underscore_list[number] = target_word[number]
            print(f"The letter {guessed_letter} is in the word.\n")
    else:
        print(f"The letter \"{guessed_letter}\" was already guessed.\nPlease guess again.")
if player_lives < 1:
    print(f"You lose. The chosen word was \"{target_word}\".")
else:
    print(f"You win! The chosen word was \"{target_word}\".")