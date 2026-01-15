class Word():
    def __init__(self, word):
        self._word = word
        self._guesses = 6
        self.pairs = []
        self.triples = []
        self.getPairs()

    def __str__(self):
        return self._word

    def getGuess(self, wordlist):
        guess = input('Please enter your guess: ')
        if guess not in wordlist:
            raise ValueError('Please guess a proper/ more common word!')
        if not guess.isalpha():
            raise ValueError('Please enter only alphabetical characters.')
        return guess.lower()

    def word_check(self, guess, user):
        guessed = []
        paircheck = []      #holds letters that occur twice and have been guessed twice
        
        count = 0
        if len(guess) != len(self._word):
            raise ValueError(f'Guess must be {len(self._word)} letters exactly!')
        for i in range(len(self._word)):
            if self._word[i] == guess[i]:
                print('<hit>', end=' ')
                count += 1       
                guessed.append(guess[i])     
            elif guess[i] in self._word:
                if guess[i] in self.pairs or guess[i] in self.triples:
                    if guess[i] in guessed:
                        if guess[i] in paircheck:
                            #guessed twice already
                            print('<miss>', end=' ')
                        else:#guessed once before
                            rest_of_guess = guess[i:]
                            rest_of_word = self.word[i:]
                            for n in range(len(rest_of_guess)):
                                check = False
                                if rest_of_guess[n] == rest_of_word[n]:
                                    print('<miss>', end=' ')
                                    check = True
                                    break
                                
                            if guess[i] not in self.triples:
                                paircheck.append(guess[i])
                            if not check:
                                print('<near>', end=' ')
                    else:#not guessed yet
                        guessed.append(guess[i])
                        print('<near>', end=' ')           
                else:
                    if guess[i] in guessed:
                        print('<miss>', end=' ')
                    else:
                        guessed.append(guess[i])
                        print('<near>', end=' ')
            else:
                print('<miss>', end=' ')
        if count == len(self._word):
            print(f'You win! The word was: {self._word}. \nYou won with {self._guesses-1} guesses remaining!')
            user.points += (self._guesses * 10)
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

    def getPairs(self):
        letters = []
        for char in self.word:
            if char not in letters:
                letters.append(char)
            elif char in self.pairs:
                self.triples.append(char)
                self.pairs.remove(char)
            else:
                self.pairs.append(char)

    def GetWord(self):
        return self._word
    
    def SetWord(self, new):
        self._word = new

    def getGuesses(self):
        return self._guesses
    
    word = property(GetWord, SetWord)
    guesses = property(getGuesses)

def test():
    word = Word('axplp')
    print(word.pairs)
    word.word_check('hlleo', '')
    word.word_check('yee5t', '')
    word.word_check('apxpp', '')

if __name__ == '__main__':
    test()