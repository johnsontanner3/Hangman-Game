'''
Created on Oct 20, 2016

@author: Tanner Johnson
'''
import random

def fileToStringList(filename):
    """
    filename is a file of strings, 
    returns a list of strings, each string represents
    one line from filename
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist
    

def getPossiblePhrases(wordList, length):
    '''
    returns a list of movie titles of with number of words length
    '''
    wordList = [word for word in wordList if len(word.split()) == length]
    return wordList
     
# def getPossibleWords(wordlist,length):
#     """
#     returns a list of words from wordlist having a 
#     specified length 
#     """
#     wordlist = [word for word in wordlist if len(word) == length]
#     return wordlist

def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String with spaces between each character
    '''
    return ' '.join(wordList)

def guessStart(phrase):
    '''
    returns a list of single characters '_' for each alphabetical character
    in the movie title. will not mutate non-alphabetical characters. 
    '''
    phrase_List = []
    for ch in phrase:
        if ch.isalpha():
            phrase_List.append("_")
        else:
            phrase_List.append(ch)
    return phrase_List
#     return ['_']*len(phrase)             # is this right??

def updateLetter(guessList,wordToGuess, letter):
    '''
    wordToGuess is the movie the user is trying to guess.
    guessList is the movie to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed. 
    
    Modify guessList to include letter in its proper locations if 
    letter is in wordToGuess.
    
  
    '''

    if letter in wordToGuess.lower():
        idxsList = [i for i, ch in enumerate(wordToGuess.lower()) if ch == letter]  #list of letter index positions in wordToGuess        
        for n in idxsList:
            guessList[n] = letter


def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    #setup for game
    guessLength = int(raw_input("how many words to guess? "))                       # num of words in title
    if guessLength < 1:
        print "The word must be at least three characters long. Try again!"        #how do we make this print? 
        quit()                                                                      # cool quit() function!
    howManyMisses = int(raw_input("how many misses allowed? "))
    print "\n"
    wordsOfLength = getPossiblePhrases(words,guessLength)                       # phrases with this many words
    wordToGuess = random.choice(wordsOfLength)                                  # choose random phrase, still string
    guessList = guessStart(wordToGuess)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    misses = 0
    
    # start the guessing
    while True:
        wordsLeft = len([word for word in "".join(guessList).split(" ") if "_" in word])
        if guessList.count('_') == 0:
            # all letters guessed
            break
        if misses == howManyMisses:           
            break
        print "guessed so far:", displayGuess(guessList)
        print "letters not guessed:", alphabet
        letter = raw_input("guess a letter or enter + to guess movie: ")
        print "number of letter misses left:", howManyMisses - misses       
        print "number of words left to complete:", wordsLeft
        updateLetter(guessList, wordToGuess, letter)
        if letter == "+":
            enterWord = raw_input("enter movie name: ")
            if enterWord.lower() == wordToGuess.lower():
                print "You win! You guessed the movie", wordToGuess, " :)"
                quit()                                                              # quit() at it again
            else:
                print "You guessed the wrong movie. Movie was", wordToGuess, " :("
                quit()                                                              # ^retweet                
        if letter in wordToGuess.lower():   
            print "you guessed a letter!"
        elif letter not in wordToGuess.lower():
            print "that's a miss."
            misses += 1
        print "\n"
        alphabet = "".join(alphabet.split(letter))
     
    # game over
    if guessList.count('_') == 0:
        print "You win! You guessed the movie", wordToGuess, " :)"
    else:
        print "You lost, movie was", wordToGuess, " :("
    print "You missed", misses, "times."

if __name__ == '__main__':
    words = fileToStringList('movies.txt')
    print "number of movies is", len(words) 
    playGame(words)
    
