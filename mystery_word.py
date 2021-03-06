import random

from pyparsing import Word

# attempting to generate random word 
def generate_word():
    with open("words.txt") as file_word:
        word_options = file_word.readlines()
        # print(f'word options: {word_options}')
        computer_word = random.choice(word_options).replace("\n", "")
        # print(f'computer word: {computer_word}')
        return computer_word

def make_word_into_list(computer_word):
    word_as_list = []
    for letter in computer_word:
        word_as_list.append(letter)
    # print(f'word as list: {word_as_list}') 
    return word_as_list  

def make_display(word_as_list): 
    display = [(letter.replace(letter, "_")) for letter in word_as_list] 
    print(' '.join(display))   
    return display
    # to call retreive word_as_list() as a variable first, then use that variable when calling display_word   

def get_guess():
    user_guess = input('Guess a letter: ')  
    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()
        # print(f'You guessed {user_guess}')
        return user_guess
    else:    
        print('Your guess is not a single letter.')   
        return get_guess()    
        # ^ you have to specify that you want to call the function again, but also return what the function has made. because we learned this today when it didn't work.      

def play_game():
    computer_word = generate_word()
    # run generate word. computer_word is the thing generate_word made. should be "dream" for now, later will be random word from file
    word_as_list = make_word_into_list(computer_word)
    # run make_word_into_list and retrieve the thing it made, calling it word_as_list. should be ["d", "r", "e", "a", "m"]
    display = make_display(word_as_list)
    # display = the thing make_display made. should be ["_", "_", "_", "_", "_"] 
    incorrect_letters = []
    letters_guessed = []
    # will store user_guess letters here if they are not in the word. 
    while len(incorrect_letters) < 8 and "_" in display:
        user_guess = get_guess()
        if user_guess in letters_guessed: 
            print(f'You already guessed {user_guess}. Please guess a new letter.')
            get_guess()
        else:     
            letters_guessed.append(user_guess)
        # user_guess = the thing get_guess made. should be a single, lowercase letter

        if user_guess not in word_as_list:
            incorrect_letters.append(user_guess)
            print(f'incorrect guesses: {", ".join(incorrect_letters)}')
            print(f'You have {8 - len(incorrect_letters)} incorrect guesses remaining.')

        display = [(letter.replace(letter, "_")) if letter not in letters_guessed else letter for letter in word_as_list]
        print(" ".join(display))

        # if "_" not in display:
        #     print(f'Congratulations! You won! The mystery word was {computer_word}')


    print(f'Game Over! The mystery word was {computer_word}')    
        # now something to tally incorrect letters 
        # incorrect_letters = [(letter) if letter not in word_as_list else print() for letter in letters_guessed]
        # print(f'incorrect_letters {incorrect_letters}')
    
if __name__ == "__main__":
    play_game()