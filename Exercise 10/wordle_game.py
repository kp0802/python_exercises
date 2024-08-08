import requests
import random
from colorama import Back, Style, init

# Initialize colorama
init(autoreset=True)

def fetch_words_from_gist():
    try:
        url = 'https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt'
        response = requests.get(url, verify = False)
        response.raise_for_status()  

        words = response.text.splitlines()  

        return words
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Gist content: {e}")
        return None

def get_random_word(words):
    return random.choice(words)

def check_word(word, target_word):
    for i in range(5):
        if word[i] == target_word[i]:
            print(Back.GREEN + f' {word[i]} ', end=' ')
        elif word[i] in target_word:
            print(Back.YELLOW + f' {word[i]} ', end=' ')
        else:
            print(Back.BLACK + f' {word[i]} ', end=' ')

    print(Style.RESET_ALL)
    return word == target_word

def wordle_game():
    words = fetch_words_from_gist()

    if words is None:
        print("Failed to fetch words from Gist.")
        return

    print("\nWelcome to Wordle!\n")
    print("You will get 6 attempts to guess the 5 letter word.")
    print("Each letter will be colored based on its position:")
    print(Back.GREEN + " Green " + Style.RESET_ALL + " for correct letter in correct position.")
    print(Back.YELLOW + " Yellow " + Style.RESET_ALL + " for correct letter in incorrect position.")
    print("Letters that are not in the word will not be colored.")
    print("\nGood luck!")

    word_to_guess = get_random_word(words)
    print(word_to_guess)
    words_guessed = []  
    max_attempts = 6
    attempt = 0

    while attempt < max_attempts:
        guess = input("\nEnter your guess: ").strip().lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if guess in words_guessed:
            print("You have already guessed this word. Try a different one.")
            continue
        print()
        for guessed_word in words_guessed:
            check_word(guessed_word, word_to_guess)
        
        words_guessed.append(guess)
        attempt += 1

        if check_word(guess, word_to_guess):
            print(f"\nCongratulations! You've guessed the word correctly in {attempt} attempt(s).")
            print("\nDo you want to play again?")
            choice = int(input("Enter 1 if Yes and 0 if No: "))
            if choice:
                wordle_game()
            break
    else:
        print(f"\nSorry, you've used all attempts. The word was: {word_to_guess}")
        print("\nDo you want to play again?")
        choice = int(input("Enter 1 if Yes and 0 if No: "))
        if choice:
            wordle_game()

# Example of how to call the function
wordle_game()
