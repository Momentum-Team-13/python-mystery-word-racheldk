import random


'''attempting to generate random word 
def generate_word():
    file = open("words.txt")
    print(repr(file.readline()))
    computer_word = random.choice(list)
    print(f'computer word: {computer_word}')
    return computer_word'''


def make_word_into_list(computer_word):
    word_as_list = []
    for letter in computer_word:
        word_as_list.append(letter)
    print(f'word as list: {word_as_list}') 
    return word_as_list  


'''The code below might be helpful....but I'm really not sure.
I was trying to make a dicitonary of dictionaries for the letter, then 
we could choose the second value in the dictionary if the letter was guessed?'''
def display(word_as_list):
    letters = {}
    for letter in word_as_list:
        letters[letter] = dict(["_ ", (letter)])
    print(dict)
    # print('_ '*len(word_as_list))


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



def compare_guess_to_word(guess, word):
    # this will take user_guess variable and computer_word variable
    if guess in word:
        print(f'{guess} is in the mystery word')
        # change display to show where the guess is
    else:
        print(f'{guess} is not in the mystery word.')
        #decrement number of guesses left or add to increasing listof guesses? ????where to store guesses - can a function 
    return guess       


def play_game():
    computer_word = "dream"
    remaining_guesses = 8
    word_as_list = make_word_into_list(computer_word)
    display(word_as_list)
    # the stuff below will be inside of a loop
    while remaining_guesses > 0:
        # while loop: keep going until the user has reached 0 remaining guesses
        user_guess = get_guess()
        compare_guess_to_word(user_guess, computer_word)
        # ?? decrement remaining guesses here so that it'll change within the while loop



if __name__ == "__main__":
    play_game()