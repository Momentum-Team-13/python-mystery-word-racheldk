computer_word = "dream"

def play_game():
    pass

def get_guess():
    user_guess = input('Guess a letter: ') 
    if len(user_guess) >1:
        print('Your guess is too long.')
        get_guess()
    elif user_guess.isalpha:
        user_guess = user_guess.lower()
        print(f'You guessed {user_guess}')
        return user_guess
    else:    
        print('Your guess is not a letter.')   
        get_guess()

get_guess()




if __name__ == "__main__":
    play_game()
