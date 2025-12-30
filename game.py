import random as rand
from word import Word

class Game():
    def __init__(self, words):
        self.words = words 
        self._points = 0
        self._difficulty = 5

    def chooseWord(self, length):
        word = rand.choice(self.words)
        while len(word) != length:
            word = rand.choice(self.words)

        return word

    def createGame(self):
        self.chooseDifficulty()
        wordinit = self.chooseWord(self._difficulty)

        word = Word(wordinit)

        print(word.word)
        
        gameOn = True

        while gameOn:
            gameOn = word.word_check(word.getGuess())
        #NB handle points system
        #need add shelving/ pickling to maintain local leaderboard
            
        
        continuegame = input('Press enter/ return to continue with a new word.')
        if continuegame == '':
            self.createGame()
        return

    def chooseDifficulty(self):
        self._difficulty = input('Choose the length of the word (min 5), or leave blank for Traditional Wordle: ')
        
        if self._difficulty == '':
            self._difficulty = 5
        else:
            self._difficulty = int(self._difficulty)

    def getPoints(self):
        return self._points
    
    def setPoints(self, new):
        self._points = new

    points = property(getPoints,setPoints)