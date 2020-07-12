def check_letter(word_copy, index, letter = None):
    '''
    Will return whether
    '''
    vowel = ['a','e','i','o','u']
    for i in range(len(word_copy)):
        if ((word_copy[i] in vowel) or (word_copy[i] == ' ') or (word_copy[i].isdigit()) or (not word_copy[i].isalnum()) or (word_copy[i] == letter)) and i not in index:
            index.append(i)
    return index

def reveal(index, word):
    '''
    Will reveal words as necessary
    '''
    i = 0
    while i < len(word):
        if i in index:
            print(word[i], end='')
        else:
            print('*',end='')
        i += 1
    print()

    return


def game(word):
    '''
    Will make a copy of the game word and handle hiding of non-vowel alphabets
    Also keeps tarck of rightly guessed values.
    '''
    tries = 7
    word_copy = word.lower()
    used = list()   # List of used letters to avoid repitition
    index = list()  # List of index positions that have to be revealed.
    index = check_letter(word_copy, index)
    reveal(index, word)

    while tries > 0:
        # print('index',index)
        if len(index) == len(word):
            print('Congratulations, you have guessed the word correctly')
            print(word)
            return

        while True:
            letter = input('Guess a letter\n\n').lower()
            if letter.isalpha() and letter not in used:
                if letter in ['a','e','i','o','u']:
                    print('You have entered a vowel. Please enter only consonants')
                    continue
                else:
                    used.append(letter)
                    break
            elif letter in used:
                print('You have previously selected {}'.format(letter))
                continue
            else:
                print('Please enter only an alphabet')
                continue

        if letter in word_copy:
            index = check_letter(word_copy, index, letter)
            print('Number of tries remaining: {}\n'.format(tries))
            reveal(index, word)
            continue
        else:
            tries -= 1
            print('The letter does not exist in the movie title')
            print('Number of tries remaining: {}\n'.format(tries))
            reveal(index, word)

    if tries < 1:
        print('You have run out of tries\nYou lost')
        print('The movie was: {}'.format(word))
        return

if __name__ == '__main__':
    game('The Shawshank Redemption')
