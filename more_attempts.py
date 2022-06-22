import random

# attempting to generate random word 
def generate_word():
    with open("test-word.txt") as file_word:
        computer_word = file_word.read().replace("\n", "")
        print(f'computer word: {computer_word}')
        return computer_word

def make_word_into_list(computer_word):
    word_as_list = []
    for letter in computer_word:
        word_as_list.append(letter)
    print(f'word as list: {word_as_list}') 
    return word_as_list  

def display_word(word_as_list): 
    display = [(letter.replace(letter, "_ ")) for letter in word_as_list] 
    print(f'display: {display}')   
    return display
    # to call retreive word_as_list() as a variable first, then use that variable when calling display_word

def get_guess():
    user_guess = input('Guess a letter: ')  
    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()
        print(f'You guessed {user_guess}')
        return user_guess
    else:    
        print('Your guess is not a single letter.')   
        return get_guess()    
        # ^ you have to specify that you want to call the function again, but also return what the function has made. because we learned this today when it didn't work. 

def compare_guess_to_word(user_guess, word_as_list, display):
    # this will take user_guess variable and computer_word variable
    if user_guess in word_as_list:
        print(f'{user_guess} is in the mystery word')
        display = [(letter.replace("_ ", user_guess)) for letter in word_as_list]
        print(display)
        # change display to show where the guess is
    else:
        print(f'{user_guess} is not in the mystery word.')
        #decrement number of guesses left  
    return user_guess       

def play_game():
    computer_word = generate_word()
    print(f'computer word type: {type(computer_word)}')
    guesses_made = []
    word_as_list = make_word_into_list(computer_word)
    display = display_word(word_as_list)
    # the stuff below will be inside of a loop
    while len(guesses_made) <= 8:
        # while loop: keep going until the user has reached 0 remaining guesses
        user_guess = get_guess()
        compare_guess_to_word(user_guess, word_as_list, display)
        # ?? decrement remaining guesses here so that it'll change within the while loop



if __name__ == "__main__":
    play_game()