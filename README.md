[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/not-a-bug-a-feature.svg)](https://forthebadge.com)  

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)
# HangMan_Game
Hang-Man game in Python. A webscrapper scraps the IMDB top 250 movies list and creates a file containing the film titles. A movie is selected at random and the player has to guess it using consonants with a maximum of 7 incorrect tries.
The vowels and non-alphabet characters are visible, while the rest of the characters are hidden by an asterisk. The player may select a minimum title length for the game.
The player may exit at the end of any round. The player has to guess one consonant at a time. The game informs in case a consonant is repeated by the player or a non-consonant is entered.

## Getting Started
Download the whole repository and save it to a folder on your PC. Make sure you have pre requisites installed. Run the [hangman.py](hangman.py) and the game will start. The [movies_names.txt](movies_names.txt) is non-essential as the web-scrapper will create/update it anyway when you run the game.

### Prerequisites
Things you need to install.
```
Python 3
```
### Running the Program
Go to the location of the [hangman.py](hangman.py) on the command line. To run it enter the following.
On Windows:
```
python hangman.py
```
On Linux/Mac:
```
python3 hangman.py
```
Follow the onscreen instructions and play.

### Built with
* Python

### Author
* Shashwat

### Acknowledgements
* I made this as a personal project to learn and have fun. It was built to practise web-scrapping as well as modular programs.
