'''
Created on Nov 23, 2016

@author: Tanner Johnson 
'''
import random

def fileToStringList(filename):
    """
    filename is a file of strings, 
    returns a list of strings, each string represents
    one line from filename. source of our possible words
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist
    
     
def getPossibleWords(wordlist,length):
    """
    returns a list of words from wordlist having a 
    specified length 
    """
    wordlist = [word for word in wordlist if len(word) == length]
    return wordlist

def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(wordList)

def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as word
    '''
    return ['_']*len(word)

def updateLetter(guessList,wordToGuess, letter):
    '''
    wordToGuess is the word the user is trying to guess.
    guessList is the word to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed. 
    
    Modify guessList to include letter in its proper locations if 
    letter is in wordToGuess.
    
    For example, if the wordToGuess is "baloney" and so far only a and
    e have been guessed, then guessList is ['_','a','_','_','_','e','_']
    If letter is 'o', then guessList is modified to now be:
    ['_','a','_','o','_','e','_']
    
    '''

    if letter in wordToGuess:
        idxsList = [i for i, ch in enumerate(wordToGuess) if ch == letter]  #list of letter index positions in wordToGuess        
        for n in idxsList:
            guessList[n] = letter


def update(wordList, letter, guessList):
    '''
    wordList = list of current valid words
    letter = letter just guessed
    guessList = as a list 
    use this for every guess to process every word from wordList
    build a dictionary will keys for all possibilities
    will return the new list of words -- based on key with max number of values
    from that list, choose one randomly
    '''
    listOfPossibilities = [] # list of strings 
    xx = []
    for word in wordList:
        newlist = guessList[:]
        if letter in word:
            yy = [i for i, ch in enumerate(word) if ch == letter] # will have to set, list for this b/c duplicates
            for i in yy:
                newlist[i] = letter
        elif letter not in word:
            newlist = newlist
        xx.append(("".join(newlist), word))
    listOfPossibilities.extend(xx)
    d = {}
    for (key, word) in listOfPossibilities:
        if key not in d:
            d[key] = []
        d[key].append(word)

    maxNum = max([len(v) for k,v in d.iteritems()])
    return [v for k,v in d.iteritems() if len(v) == maxNum][0]


def updateSeeDict(wordList, letter, guessList):
    '''
    creates the same dictionary as update function,
    but prints out each key with number of values for testing mode
    '''
    listOfPossibilities = [] # list of strings 
    xx = []
    for word in wordList:
        newlist = guessList[:]
        if letter in word:
            yy = [i for i, ch in enumerate(word) if ch == letter] # will have to set, list for this b/c duplicates
            for i in yy:
                newlist[i] = letter
        elif letter not in word:
            newlist = newlist
        xx.append(("".join(newlist), word))
    listOfPossibilities.extend(xx)
    d = {}
    for (key, word) in listOfPossibilities:
        if key not in d:
            d[key] = []
        d[key].append(word)
    print "Dictionary of categories and # of words:"
    for k,v in d.iteritems():
        print k, len(v)


def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    This is for TESTING mode--prints more information to help debug
    '''
    #setup for game
    guessLength = int(raw_input("how many letters in word to guess? "))
    if guessLength < 3:
        print "The word must be at least three characters long. Try again!"        #how do we make this print? 
        quit()                                                                      # cool quit() function!
    howManyMisses = int(raw_input("how many misses allowed? "))
    print "\n"
    wordsOfLength = getPossibleWords(words,guessLength)    
    wordToGuess = random.choice(wordsOfLength)       # do this to START the program, the initial word
    guessList = guessStart(wordToGuess)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    misses = 0
    
    # start the guessing
    while True:
        if guessList.count('_') == 0:
            # all letters guessed
            break
        if misses == howManyMisses:           
            break
        print "guessed so far:", displayGuess(guessList)
        print "letters not guessed:", alphabet
        print "number of misses left:", howManyMisses - misses       
        letter = raw_input("guess a letter or enter + to guess a word: ")
#         updateLetter(guessList, wordToGuess, letter)
        if letter == "+":
            enterWord = raw_input("enter word: ")
            if enterWord == wordToGuess:
                print "You win! You guessed the word", wordToGuess, " :)"
                quit()                                                              # quit() at it again
            else:
                print "You guessed the wrong word. Word was", wordToGuess, " :("
                quit()                                                              # ^retweet
        else:
            
            wordToGuess = random.choice(update(wordsOfLength, letter, guessList)) # update wordToGuess
            updateSeeDict(wordsOfLength, letter, guessList)

            wordsOfLength = update(wordsOfLength, letter, guessList) # update list of words 
            updateLetter(guessList, wordToGuess, letter)
            if letter in wordToGuess:
                print "you guessed a letter!"
            elif letter not in wordToGuess:
                print "that's a miss."
                misses += 1
        print "(secret word:", wordToGuess, ")", "# words possible", len(update(wordsOfLength, letter, guessList)) #, updateSeeMaxNum(wordsOfLength, letter, guessList)
        print "\n"
        alphabet = "".join(alphabet.split(letter))
     
    # game over
    if guessList.count('_') == 0:
        print "You win! You guessed the word", wordToGuess, " :)"
    else:
        print "You lost, word was", wordToGuess, " :("
    print "You missed", misses, "times."


def playGame2(words):
    '''
    Play the game. Let the user know if they won or not.
    This is for GAME mode.
    '''
    #setup for game
    guessLength = int(raw_input("how many letters in word to guess? "))
    if guessLength < 3:
        print "The word must be at least three characters long. Try again!"        #how do we make this print? 
        quit()                                                                      # cool quit() function!
    howManyMisses = int(raw_input("how many misses allowed? "))
    print "\n"
    wordsOfLength = getPossibleWords(words,guessLength)    
    wordToGuess = random.choice(wordsOfLength)       # do this to START the program, the initial word
    guessList = guessStart(wordToGuess)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    misses = 0
    
    # start the guessing
    while True:
        if guessList.count('_') == 0:
            # all letters guessed
            break
        if misses == howManyMisses:           
            break
        print "guessed so far:", displayGuess(guessList)
        print "letters not guessed:", alphabet
        print "number of misses left:", howManyMisses - misses       
        letter = raw_input("guess a letter or enter + to guess a word: ")
#         updateLetter(guessList, wordToGuess, letter)
        if letter == "+":
            enterWord = raw_input("enter word: ")
            if enterWord == wordToGuess:
                print "You win! You guessed the word", wordToGuess, " :)"
                quit()                                                              # quit() at it again
            else:
                print "You guessed the wrong word. Word was", wordToGuess, " :("
                quit()                                                              # ^retweet
        else:
            
            wordToGuess = random.choice(update(wordsOfLength, letter, guessList)) # update wordToGuess
            wordsOfLength = update(wordsOfLength, letter, guessList) # update list of words 
            updateLetter(guessList, wordToGuess, letter)
            if letter in wordToGuess:
                print "you guessed a letter!"
            elif letter not in wordToGuess:
                print "that's a miss."
                misses += 1
        print "\n"
        alphabet = "".join(alphabet.split(letter))
     
    # game over
    if guessList.count('_') == 0:
        print "You win! You guessed the word", wordToGuess, " :)"
    else:
        print "You lost, word was", wordToGuess, " :("
    print "You missed", misses, "times."
    
    


if __name__ == '__main__':
    words = fileToStringList('lowerwords.txt')
    print "game (g) or testing (t) mode?"
    chooseOption = raw_input("g or t: ")
    print "Welcome to hangman"
    if chooseOption == "t":
        playGame(words)
    elif chooseOption == "g":
        playGame2(words)

    
    