'''
Scraps movie names from the IMDB top 250 movies page, and saves them in a text file.
Other data like release year, rating, vote, star cast etc. are not used for the HangMan game,
and hence are not being stored.
'''

def scrap_imdb():

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import requests
    import ssl
    import re

    # Ignore SSL certification errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Get IMDB's Top 250 data
    url = 'https://www.imdb.com/chart/top'
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    movies = soup.select('td.titleColumn')

    # Create File
    fname = 'movie_names.txt'
    file = open(fname,'w')

    # Add each movie name to the file.
    for index in range(len(movies)):
        movie_string = movies[index].get_text() # This gives the string separated by newlines.
        movie = (' '.join(movie_string.split()).replace('.', ''))   # This puts the string in a single line
        # Eg- 1 Shawshank Redemption (1994)
        movie_title = movie[len(str(index))+1:-7]   # Removes index number from title. and removes last 7 positions i.e. year
        movie_title = movie_title.strip()
        file.write(movie_title+'\n')

    # Close file connection.
    file.close()
    return fname

if __name__ == '__main__':
    words = scrap_imdb()
    print('The file {} has been created.'.format(words))
