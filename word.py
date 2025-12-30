class Word():
    def __init__(self, word):
        self._word = word
        self._guesses = 6

    def getGuess(self):
        guess = input('Please enter your guess: ')
        return guess

    def word_check(self, guess, user):
        count = 0
        if len(guess) != len(self._word):
            raise ValueError(f'Guess must be {len(self._word)} letters exactly!')
        for i in range(len(self._word)):
            if self._word[i] == guess[i]:
                print('<hit>', end=' ')
                count += 1
            elif guess[i] in self._word:
                print('<near>', end=' ')
            else:
                print('<miss>', end=' ')
        if count == len(self._word):
            print(f'You win! The word was: {self._word}. \nYou won with {self._guesses-1} guesses remaining!')
            user.points = user.points + (self._guesses * 10)
            user.guesses += (7-self._guesses)
            return False
        
        self._guesses -= 1
        if self._guesses == 0:
            print(f'You lose! The word was: {self._word}')
            user.points -= 10
            user.guesses += 6
            return False
        if self._guesses == 1:
            print(f'\nYou have {self._guesses} guess left')
            return True
        else: 
            print(f'\nYou have {self._guesses} guesses left')
            return True

    def GetWord(self):
        return self._word
    
    def SetWord(self, new):
        self._word = new

    def getGuesses(self):
        return self._guesses
    
    word = property(GetWord, SetWord)
    guesses = property(getGuesses)