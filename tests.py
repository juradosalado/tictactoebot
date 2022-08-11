
from tictactoe import EMPTY, player, actions, result, winner, terminal, utility, minimax, actions2
x = 0

def functionX():
    y=2
    return 1

def function2():
    x= functionX()
    return x +1

function2()
functionX()

X = "X"
O = "O"
EMPTY = None
board = [[X, EMPTY, O],
            [X, X, O],
            [EMPTY, X, EMPTY]]

#player(board)

print(actions(board))
print(actions2(board))

tupleTest = (0,1)
#result(board, tupleTest)

#print(winner(board))

#print(terminal(board))

#print(utility(board))

#print(minimax(board))