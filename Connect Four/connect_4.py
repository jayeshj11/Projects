import random  
from main import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        x = self.checker
        s = 'Player ' + x +' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return x

    def max_score_column(self, scores):
         best_score = max(scores)
         count = []
         for x in range(len(scores)):
             if  best_score <= scores[x]:
                 best_score = scores[x]
                 count += str(x)
         if self.tiebreak == 'RANDOM':
             count_choice = random.choice(count)
             count_choice = int(count_choice)
             return count_choice
         elif self.tiebreak == 'LEFT':
             count_choice = count[0]
             count_choice = int(count_choice)
             return count_choice
         elif self.tiebreak == 'RIGHT':
             count_choice = count[-1]
             count_choice = int(count_choice)
             return count_choice

    def scores_for(self, board):
        count = [50] * board.width
        for w in range(board.width):
            if board.can_add_to(w) == False:
                count[w] = -1
            elif board.is_win_for(self.checker):
                count[w] = 100
            elif board.is_win_for(self.opponent_checker()):
                count[w] = 0
            elif self.lookahead == 0:
                count[w] = 50
            else:
                board.add_checker(self.checker,w)
                op = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1)
                x = op.scores_for(board)
                a = max(x)
                if a == 0:
                    a = 100
                elif a == 100:
                    a = 0
                elif a == 50:
                    a = 50
                count[w] = a
                board.remove_checker(w)
        return count

    def next_move(self, board):
        x = str(self)
        x = x[-1]
        a = self.scores_for(board)
        b = self.max_score_column(a)
        board.add_checker(x, b)
        return b


def game():
    print()
    print('Hello and welcome to Connect Four!')
    print()
    '''------------------------------------------'''
    print('Choose one of the following options for Player 1 (X)')
    print('    1. Human Player')
    print('    2. Random Computer Player')
    print('    3. AI Computer Player')
    print()
    player1 = int(input('Your choice for Player 1 (X): '))
    print()
    assert(player1 == 1 or player1 == 2 or player1 == 3)
    if player1 == 1:
        p1 = Player('X')
    elif player1 == 2:
        p1 = RandomPlayer('X')
    else:
        diff = int(input('Choose a level of difficulty (1,2,3,4,5): '))
        assert(diff == 1 or diff == 2 or diff == 3 or diff==4 or diff==5)
        p1 = AIPlayer('X', 'RANDOM', diff)
    '''------------------------------------------'''
    print('Choose one of the following options for Player 2 (O)')
    print('    1. Human Player')
    print('    2. Random Computer Player')
    print('    3. AI Computer Player')
    print()
    player2 = int(input('Your choice for Player 2 (O): '))
    print()
    assert(player2 == 1 or player2 == 2 or player2 == 3)
    if player1 == 1:
        p2 = Player('O')
    elif player1 == 2:
        p2 = RandomPlayer('O')
    else:
        diff = int(input('Choose a level of difficulty (1,2,3,4,5): '))
        assert(diff == 1 or diff == 2 or diff == 3 or diff==4 or diff==5)
        p2 = AIPlayer('O', 'RANDOM', diff)
 
    connect_four(p1,p2)

game()