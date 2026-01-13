import random as rand
from word import Word
from user import User
import shelve

class Game():
    def __init__(self, words):
        self.words = words 
        self._difficulty = 5
        self._usr = User()      #will be a user object to handle errors in login/ registration

    def login(self, name= False):
        if not name:
            print('No username provided, beginning registration.')
            self.register()
        else:
            db = shelve.open('users')
            if name in db:
                self._usr = db[name]
                db.close()
            else:
                db.close()
                self.register()

    def register(self):
        name = input('Please enter a new username: ')
        if name == '':
            self.register()
        user = User(name)
        db = shelve.open('users')
        db[name] = user
        self._usr = user
        db.close()

    def chooseWord(self, length):
        word = rand.choice(self.words)
        while len(word) != length:
            word = rand.choice(self.words)

        return word

    def createGame(self):
        db = shelve.open('users', writeback=True)
        self.chooseDifficulty()
        wordinit = self.chooseWord(self._difficulty)

        word = Word(wordinit)

        #print(word.word)
        
        gameOn = True
        
        while gameOn:
            try:
                gameOn = word.word_check(word.getGuess(self.words), self._usr)   #NB getGuess() used to get user input, not usual getter
            except ValueError as e:
                print(e)
            
        db[self._usr.name] = self._usr
        continuegame = input('Press enter/ return to continue with a new word.')
        if continuegame == '':
            db.close()
            self.createGame()
            return
        print('LEADERBOARD')
        users = []
        for key in db:
            users.append((db[key], db[key].points))
        users.sort(key= lambda x : x[1], reverse=True)
        for tup in users:
            print(tup[0])
        db.close()
        return 

    def chooseDifficulty(self):
        self._difficulty = input('Choose the length of the word (min 5), or leave blank for Traditional Wordle: ')
        
        if self._difficulty == '':
            self._difficulty = 5
        else:
            self._difficulty = int(self._difficulty)