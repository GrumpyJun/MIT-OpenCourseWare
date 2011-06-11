# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 5F
# Student: May Pongpitpitak
# June 9, 2011

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 1)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()



# TO DO: your code begins here!

def start_game(word_list):
    print("Welcome to Ghost!")

    # Create player
    player1 = 'Player 1'
    player2 = 'Player 2'
    
    # Initiate/clear word fragment variable
    wordFragment = ''
    
    # Player 1 initiate the game
    print("The game starts with Player 1")
    wordFragment = new_turn(player1, wordFragment)
    gameCont = check_wordFragment(wordFragment, wordlist)
    
    while gameCont == True or len(wordFragment) <= 3:
        # Player 2 goes next
        wordFragment = new_turn(player2, wordFragment)
        gameCont = check_wordFragment(wordFragment, wordlist)
        if gameCont == False and len(wordFragment) > 3:
            print("Player 1 wins!")
            break

        # Player 1 go again
        wordFragment = new_turn(player1, wordFragment)
        gameCont = check_wordFragment(wordFragment, wordlist)
        if gameCont == False and len(wordFragment) > 3:
            print("Player 2 wins!")
            break



##def create_player(totalPlay):
##    """
##    For if more than two players is desired
##    """
##
##    players =[]
##    
##    for currentPlayer in range(totalPlay):
##        numPlayer = "Player " + str(currentPlayer)
##        players.append(numPlayer)
##
##    return(players)



def new_turn(player, wordFragment):
    """
    Perform task neccesary for each turn
    """
    
    print("Current word fragment:", str.upper(wordFragment))
    print(player + "'s turn")
    nextLetter = input("Please enter a letter: ")

    if nextLetter == '.':
        exit
    else:
        wordFragment += str.lower(nextLetter)
        return(wordFragment)
    


def check_wordFragment(wordFragment, wordlist):
    """
    Check if either the word is completed or will lead up to a valid word

    return: True -- if the letter leads up to a word but doesnot complete a word
            False -- if the letter doesnot lead to a word or complete a word
    """
    for eachWord in wordlist:
        if eachWord.startswith(wordFragment) == True:
            if wordFragment == eachWord:    # Case of completed word
                print(wordFragment, "is a word")
                return False
            else:                           # Case of partial word 
                return True

    # If the letter doesnot lead to a word
    if wordFragment not in wordlist: 
        print("No word begins with", wordFragment)
        return False



if __name__ == '__main__':
    word_list = load_words()
    start_game(word_list)
