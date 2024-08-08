import requests

def get_posts():
    url = 'https://random-word-api.herokuapp.com/word'

    try:
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            random_word = response.json()[0]  # Get the first word from the list
            return random_word
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def hangman_graphic(stage):
    stages = [
        '''
         -----
         |   |
             |
             |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
             |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        '''
    ]
    return stages[stage]

def display_word(word, guesses):
  display = ""
  for letter in word:
    if letter in guesses:
      display += letter + " "
    else:
        display += " _ "
  return display.strip()

def hangman_game():
  generated_word = get_posts()
  # print()
  # print(generated_word)

  if generated_word:
      max_guesses = 6
      incorrect_guesses_made = 0

      generated_word = generated_word.lower()
      letters_guessed = set()

      print("\n",hangman_graphic(incorrect_guesses_made),display_word(generated_word, letters_guessed))

      while incorrect_guesses_made < max_guesses:
        # print()
        user_guess = input("\nGuess a letter: ").lower()

        if len(user_guess) != 1 or not user_guess.isalpha():
                print("\nPlease enter a single letter.")
                continue        

        if user_guess in letters_guessed:
            print("\nYou have already guessed this letter!")
            continue
        else:
          letters_guessed.add(user_guess)

        if user_guess in generated_word:
          print("\nCongratulations! Your guess was correct.")  
        else:
            print("\nOOPS! Wrong Guess.")
            incorrect_guesses_made = incorrect_guesses_made + 1
            print("Incorrect Guesses Made: ", incorrect_guesses_made)

        progress_made = display_word(generated_word, letters_guessed)

        print(hangman_graphic(incorrect_guesses_made),progress_made)

        if "_" not in progress_made:
          print("YOU HAVE CORRECTLY GUESSED THE WORD!!")
          print("\nWant to play the game again?")
          choice = int(input("Enter 1 if Yes and 0 if No: "))
          if(choice):
            hangman_game()
          break
          
      else:
        print(f"\nGame over! The word was '{generated_word}'.")
        print("\nWant to play the game again?")
        choice = int(input("Enter 1 if Yes and 0 if No: "))
        if(choice):
          hangman_game()
            
  else:
      print("Failed to retrieve the word.")

hangman_game()
