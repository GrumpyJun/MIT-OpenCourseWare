# MIT OpenCourseWare - Online Education
# CS 6.00 - Intro to Computer Science
# Problem set 6
# Student: May Pongpitpitak
# June 13, 2011


import random
import string
import time

VOWELS      = 'aeiou'
CONSONANTS  = 'bcdfghjklmnpqrstvwxyz'

WORD_LIST   = {}
POINTS_DICT = {}        # The dictionary of words and points is created at the beginning of the game
HAND_SIZE   = 7
TIME_LIMIT  = 0         # The time limit is either user input or calculate in the 'get_time_limit' function
k = 100

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 1) # Given code not working, changed buffering value to 1
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return(wordlist)

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
    return(freq)


# (end of helper code)
# -----------------------------------


def get_word_score(word):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    
    wordScore = 0
    for letter in word:
        wordScore += SCRABBLE_LETTER_VALUES[letter]
    
    # for bonus jackpot
    if len(word) == HAND_SIZE:
        wordScore +=50

    return(wordScore)



def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, )            # print all on the same line



def deal_hand():
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    HAND_SIZE: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand        = {}
    num_vowels  = int(HAND_SIZE / 3)             # Given code not working, casted to int
    
    for i in range(num_vowels):
        x       = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, HAND_SIZE):    
        x       = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return(hand)



def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...

    freq = get_frequency_dict(word)
    newHand = {}
    for letter in hand:
        newHand[letter] = hand[letter] - freq.get(letter,0)

    return(newHand)


def is_valid_word(word, hand):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    freq = get_frequency_dict(word)

    for letter in word:
        if freq[letter] > hand.get(letter, 0):  # Check if there's letter in hand
           return(False)

    return(word in WORD_LIST)                   # Check if the word is in the list



# -----------------------------------------------------------------------------
# Problem set 6 part 3 - 4
#
def get_words_to_points():
    """
    Return a dict that maps every word in word_list to its point value.
    """
    
    for word in WORD_LIST:
        POINTS_DICT[word] = get_word_score(word)

    return(POINTS_DICT)

    

def get_time_limit():
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
     """

    start_time  = time.time()
    
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in POINTS_DICT:
        get_frequency_dict(word)
        get_word_score(word)

    end_time    = time.time()

    return((end_time - start_time) * k)



def pick_best_word(hand):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """
    global POINTS_DICT
    
    bestWord         = '.'                      # By default if no word can be formed, it will return exit command
    currentBestScore = 0
    handDict         = get_frequency_dict(hand)
    
    for word in POINTS_DICT:                      
        if is_valid_word(word, hand):
            # Check if the current word yields better score.
            # If yes, current word is the best word.
            thisWordScore   = POINTS_DICT[word]
            if thisWordScore > currentBestScore:
                bestWord          = word
                currentBestScore  = thisWordScore
    
    return(bestWord)



# End of Problem 6 part 3 - 4
# -----------------------------------------------------------------------------
#


def play_hand(hand):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    
##    global TIME_LIMIT   = int(input("Please enter time limit in seconds: "))

    
    global TIME_LIMIT
    TIME_LIMIT      = get_time_limit()

    scoreThisHand   = 0             # Set/reset the score counter for current hand   
    totalTime       = 0             # Set/reset the timer
    
    while sum(hand.values()) > 0:       # While there are cards in hand

        print("Current hand:")
        display_hand(hand)
        
        # Add timer
        startTime   = time.time()
##        word        = input("Please enter the word to play or '.' to quit:")      # User input
        word        = pick_best_word(hand)     # Computer player
        endTime     = time.time()
        totalTime   = endTime - startTime
        print("Word entered:", word)
        print("It took %0.2d seconds to provide an answer" % totalTime)
        
        if word == '.':
            print("End game")
            print("Your total score is %0.2f points" % scoreThisHand)
            break

        else:
            # Check if the word is valid, re-enter if not
            if not is_valid_word(word, hand):
                print("The word '%s' you entered is invalid." % word)

            else:
                # If the response time exceeds the limit, the score will not count
                if totalTime <= TIME_LIMIT:
##                    currentScore = get_word_score(word, HAND_SIZE) / totalTime
                    currentScore = POINTS_DICT[word] / totalTime
                    print("This word '%s' gives you %0.2f points" % (word, currentScore))
                    scoreThisHand += currentScore
                    
                else:
                    print("Total Time exceeds %d seconds. Your score is %0.2f points" % (TIME_LIMIT, scoreThisHand))
                    break

                hand = update_hand(hand, word)
                
    
    print("Total score in this hand: %0.2f" % scoreThisHand)
    


def play_game():
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
#    print("play_game not implemented.")        # delete this once you've completed Problem #4
#    play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand()                        # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand()
            play_hand(hand.copy())
            print
        elif cmd == 'r':
            play_hand(hand.copy())
            print
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    global WORD_LIST    
    global POINTS_DICT
    
    WORD_LIST   = load_words()
    POINTS_DICT = get_words_to_points()
    
    play_game()

