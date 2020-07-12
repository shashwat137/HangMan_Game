'''
HangMan Game
The non alphabets as well as vowels are revealed.
Only consonants need to be guessed.

Dependency files : bs4, IMDBscraper.py, gameengine.py and guess_generate.py
'''

import guess_generate
import gameengine

def main():
    print('Welcome to HangMan\n')
    while True:
        start = input('Enter "y" to play and "q" to quit\n')
        if start.lower() == "q":
            print('Bye\n')
            return
        elif start == 'y':
            play_state = True

            while True:
                print('As part of game rule, you will get 7 failsafes.\nBeyond which you will lose the game\n')

                while True:
                    min_word_length = int(input('Enter the minimum number of alphabets you want in the movie to be guessed.\nNumber should be an integer value between 1 and 30\n'))
                    if min_word_length > 30 or min_word_length < 1:
                        print('Please Enter a valid range\n')
                        continue
                    else:
                        break

                selected = guess_generate.filter_movies(min_word_length)
                word_guess = guess_generate.random_movie(selected)
                print('Guess the current word')
                gameengine.game(word_guess)
                while True:
                    option1 = input('Do you want to continue playing with present word length limit?\nEnter "y" or "n"\n')
                    if option1.lower() == 'y':
                        selected.remove(word_guess)
                        if len(selected) == 0:
                            print('No more movies to select from\n')
                            play_state = False
                        else:
                            word_guess = guess_generate.random_movie(selected)
                            print('Guess the current word')
                            gameengine.game(word_guess)
                    elif option1.lower() == 'n':
                        play_state = False
                        break
                    else:
                        print('Invalid input. Enter only "y" or "n"\n')
                        continue
                if not play_state:
                    if len(selected) == 0:
                        while True:
                            option2 = input('Enter "r" if you want to restart the game. Enter "q" to quit\n').lower()
                            if option2 == 'r' or 'q':
                                break
                            else:
                                print('Invalid Input. Try again')
                                continue
                    else:
                        break

                    if option2 == 'r':
                        continue
                    else:
                        break
                else:
                    continue
        else:
            print('User input error, please try again.\n')
            continue
    return

if __name__ == '__main__':
    main()
    # Need to check if while loop at line 15 is needed.
