import tkinter as tk
from game import Game
import shelve 

higherwordlist = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 
'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 
'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 
'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful', 
'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser', 
'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen', 
'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 
'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower'
'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 
'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive', 
'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure', 
'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter', 
'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy',
'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 'friend',
'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 
'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment']

wordlist = []
inFile = open('wordle-answers-alphabetical.txt','r')
for word in inFile:
    word = word.strip()
    wordlist.append(word)
inFile.close()

for word in higherwordlist:
    wordlist.append(word)

lengths = [len(x) for x in wordlist]
print(max(lengths), min(lengths))

game = Game(wordlist)

db = shelve.open('users')
for key in db:
    print(db[key])
db.close()

name = input('Please enter your username, or leave blank for registration: ')
if name == '':
    game.register()
else:
    game.login(name)
game.createGame()