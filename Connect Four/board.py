#
# ps9pr1.py  (Problem Set 9, Problem 1)
#
# A Connect-Four Board class 
#

class Board:
    """ A class that represents the board for a game of Connect Four """

    def __init__(self, height, width):
        """ Constructor for a Board object that represents a board
            with 2 attributes: height and width 
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = '' # begin with an empty string

        # add one row of slots at a time
    
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.

        s += (2 * self.width + 1) * '-'
        s += '\n'
        s += ' '

        for col in range(self.width):
            if col > 9:
                col %= 10
            s += str(col)
            s += ' '
        
        return s

    def add_checker(self, checker, col):
        """ accepts two inputs: checker, a one-character string that
            specifies the checker to add to the board (either 'X' or 'O'), and
            col, an integer that specifies the index of the column to which the
            checker should be added and that adds checker to the appropriate
            row in column col of the board.
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        row = 0
        while self.slots[row][col] == ' ' and row + 1 < self.height: 
            row += 1
        if self.slots[row][col] != ' ':
            row += -1
            
        self.slots[row][col] = checker

    def reset(self):
        """ resets the Board object on which it is called by setting all slots
            to contain a space character.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column
            col on the calling Board object. Otherwise, it should return False.
        """
        if col < 0:
            return False
        elif col > self.width-1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
        
    def is_full(self):
        """ returns True if the called Board object is completely full of
            checkers, and returns False otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing.
        """
        row = 0
        while self.slots[row][col] == ' ' and row + 1 < self.height:
            row += 1
        if self.slots[row][col] != ' ':
            self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False


    def is_up_diagonal_win(self, checker):
        """ Checks for an up diagonal win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ Accepts a parameter checker that is either 'X' or 'O', and returns
            True if there are four consecutive slots containing checker on the
            board. Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')

        # call the helper functions and use their return values to
        # determine whether to return True or False
    
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False

