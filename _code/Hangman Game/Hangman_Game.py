# HANGMAN GAME
# -------------------
import random as r
import string as st
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return r.choice(wordlist)

# Loads the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(wordToGuess, lettersGuessed):
    '''
    wordToGuess: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of wordToGuess are in lettersGuessed;
      False otherwise
    '''
    for i in wordToGuess:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(wordToGuess, lettersGuessed):
    '''
    wordToGuess: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in wordToGuess have been guessed so far.
    '''
    guess = []
    for i in wordToGuess:
        if i in lettersGuessed:
            guess.append(i)
        else:
            guess.append('_')
    return ' '.join(guess)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lo_alphabet = st.ascii_lowercase
    choices = []
    for i in lo_alphabet:
        if i not in lettersGuessed:
            choices.append(i)
    return ''.join(choices)

def hangman(wordToGuess):
    '''
    wordToGuess: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the wordToGuess contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    mistakesMade = 0
    lettersGuessed = []
    print("Welcome to Hangman!")
    print("The word you have to guess is", len(wordToGuess), "letters long.")
    while 8 - mistakesMade > 0:
        if isWordGuessed(wordToGuess, lettersGuessed) == True:
            print("-------------")
            print("Congratulations, you won!")
            break
        else:
            print("-------------")
            print("You have", 8 - mistakesMade, "guesses left.")
            print("Available letters to choose from:", getAvailableLetters(lettersGuessed))
            guess = str(input("Please guess a letter:")).lower()
            if guess in wordToGuess and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(wordToGuess, lettersGuessed))
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(wordToGuess, lettersGuessed))
            elif guess not in wordToGuess:
                print("Oops! That letter is not in my word:", getGuessedWord(wordToGuess, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesMade += 1
        if 8 - mistakesMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", wordToGuess)
            break
        else:
            continue

wordToGuess = chooseWord(wordlist).lower()
hangman(wordToGuess)
