import random


'''attempting to generate random word 
def generate_word():
    file = open("words.txt")
    print(repr(file.readline()))
    computer_word = random.choice(list)
    print(f'computer word: {computer_word}')
    return computer_word'''

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

def make_display(word_as_list): 
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

def play_game():
    computer_word = generate_word()
    # run generate word. computer_word is the thing generate_word made. should be "dream" for now, later will be random word from file
    word_as_list = make_word_into_list()
    # run make_word_into_list and retrieve the thing it made, calling it word_as_list. should be ["d", "r", "e", "a", "m"]
    display = make_display()
    # display = the thing make_display made. should be ["_", "_", "_", "_", "_"] 
    letters_guessed = []
    # will store user_guess letters here if they are not in the word. 
    while len(letters_guessed) <=8:
        user_guess = get_guess()
        # user_guess = the thing get_guess made. should be a single, lowercase letter
        display = [(letter.replace(letter, "_")) if letter not in letters_guessed else letter for letter in word_as_list]

        '''as long as the user has guesses left, do the following things:
        1. run get_guess and keep the result
        2. update the display
            
        '''


        if user_guess in word_as_list:
            print(f'{user_guess} is in the mystery word')
            display = [(letter.replace("_ ", user_guess)) for letter in word_as_list]
            print(display)
            # change display to show where the guess is
        else:
            print(f'{user_guess} is not in the mystery word.')
            #decrement number of guesses left  
        return user_guess       
    

if __name__ == "__main__":
    play_game()