class User():
    def __init__(self, name = 'default'):
        self.name = name
        self.points = 0
        self.guesses = 0
        self.guessed_words = []

    def __str__(self):
        return f'{self.name} has scored {self.points} points and made {self.guesses} guesses!'