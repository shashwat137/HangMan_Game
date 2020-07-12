'''
Reads all movies from the text file created by IMDBscraper.
Then selects one word at random and returns it.
'''

import random
import IMDBscraper

def get_words():
    ''' Create the movie list. File name is stored in fname.'''
    fname = IMDBscraper.scrap_imdb()
    movie_list =list()
    file = open(fname, 'r')
    for line in file:
        movie_list.append(line[:-1])

    # print(movie_list)
    return movie_list

def filter_movies(min_word_length):
    '''
    Will select from a list of movies,
    the possible options based on length limits.
    Takes a integer value of minimum characters required.
    Does not consider numbers and punctuation as they are not used to guess.
    Returns a filtered list.
    '''

    movie_list = get_words()
    selected = list()
    for movie in movie_list:
        count = 0
        for character in movie:
            if character.isalpha():
                count += 1
        if count >= min_word_length:
            selected.append(movie)

    # print(selected)
    return selected

def random_movie(selected):
    '''
    Takes a filtered list of movies and selectes a particular movie from the list.
    Does not remove the movie selected at random from the list.
    The word selected must be removed from the list externally.
    '''
    index = random.randint(0, len(selected))
    return selected[index]

if __name__ == '__main__':
    print(random_movie(filter_movies(30)))
