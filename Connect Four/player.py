#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from board import Board

# write your class below

class Player:
    
    def __init__(self, checker):
        """ constructor for a Player object that represents a Player's checker
            and keeps a count of the number of moves played.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker

    def __repr__(self):
        """ represents a Player object's checker
        """
        s = 'Player ' + str(self.checker)
        return s

    def opponent_checker(self):
        """ returns the opponent's checker based on what the player's checker is
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ that accepts a Board object as a parameter and returns the column
            where the player wants to make the next move.
        """
        while True:
            x = str(self)
            x = x[-1]
            a = int(input('Enter a column: '))
            if a < board.width and a > -1:
                board.add_checker(x, a)
                return a
            else:
                print('Try again!')
