"""
Tic Tac Toe Player
"""

import math

import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def getPlayedList(board):
    playedList = []
    for row in board:
        #Add Xs and Os to playedList
        playedList.extend(row)
    return playedList


def player(board): #Checked
    """
    Returns player who has the next turn on a board.
    """
    playedList = getPlayedList(board)

    xplayed = playedList.count(X)
    oplayed = playedList.count(O)

    if oplayed<xplayed:
        return O
    else:
        return X


def actions(board): #Checked
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setRes = set()
    
    playedList = getPlayedList(board)

    for index, element in enumerate(playedList):
        if element == None:
            #add row and column to a tuple
            tupleRes = (index//3, index%3)
            setRes.add(tupleRes)
    return setRes



def result(board, action): #Checked
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    i = action[0]
    j = action[1]

    playerToPlay = player(board)

    newBoard[i][j] = playerToPlay

    print(newBoard)

    return newBoard



def winner(board): #Checked
    """
    Returns the winner of the game, if there is one.
    """
    winnerRes = None
    #Check rows
    for row in board:
        setRow = set(row)
        if len(setRow)==1:
            winnerRes = row[0]
            if winnerRes != None:
                return winnerRes

    #Check columns
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]:
            winnerRes = board[0][i]
            if winnerRes != None:
                return winnerRes
    
    #Check diagonal
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        winnerRes=board[1][1]
        if winnerRes != None:
                return winnerRes

    return winnerRes


def terminal(board): #Checked
    """
    Returns True if game is over, False otherwise.
    """
    playedList = getPlayedList(board)
    if winner(board) != None or playedList.count(None) == 0:
        return True
    else:
        return False


def utility(board): #Checked
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)== X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    if(board==initial_state()):
        return (0, 1)
    
    optimalMove = None

    if player(board)==X:
        value, action = maxValue(board)
        return action
    else:
        value, action = minValue(board)
        return action

#This two function predict what their rival is going to do next to try to win the game.
#They search an action that can lead them to victory or, if there is no such action, to a draw.
    
def maxValue(board):
    move = None
    if terminal(board):
        return utility(board), move

    v = -math.inf
    for action in actions(board):
        aux, act = minValue(result(board, action))
        if aux>v:
            v = aux
            move = action
            if v==1:
                return v, move

    return v, move

def minValue(board):
    move = None
    if terminal(board):
        return utility(board), move
    v = math.inf
    for action in actions(board):
        aux, act = maxValue(result(board, action))
        if aux<v:
            v = aux
            move = action
            if v==-1:
                return v, move
    return v, move
