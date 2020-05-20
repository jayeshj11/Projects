from board import Board
from player import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(Player, board):
    x = str(Player) + "'s"
    print(x, 'move')
    a = Player.next_move(board)
    print()
    print(board)
    print()
    z = x[-3]
    if z == 'X':
        j = 'O'
    else:
        j = 'X'
    g = str(Player)
    h = g[:-1] + 'j'
    if board.is_win_for(z) == True:
        s = g + ' wins!!!'
        print('Congratulations!')
        print(s)
        return True
    elif board.is_win_for(j) == True:
        s1 = h + ' wins!!!'
        print('Congratulations!')
        print(s1)
        return True
    else:
        if board.is_full() == True:
            s2 = "It's a tie!"
            print(s2)
            return True
        else:
            return False

class RandomPlayer(Player):
    def next_move(self, board):
        empty_list = [ ]
        f = str(self)
        f = f[-1]
        for w in range(board.width):
            if board.can_add_to(w) > -1:
                empty_list += [w]
            elif board.is_empty() == True:
                empty_list += [w]
        x = random.choice(empty_list)
        g = board.add_checker(f, x)
        return g
