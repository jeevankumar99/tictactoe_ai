"""
Tic Tac Toe Player
"""

import math
import copy

INFINTY = math.inf
X = "X"
O = "O"
EMPTY = None
move_list = []


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x, o = 0, 0
    for row in board:
        for tile in row:
            if tile == X:
                x += 1
            if tile == O:
                o += 1
    if x > o:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act_list = []
    for i in range(0, 3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                act_list.append((i, j))
    return act_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp_board = copy.deepcopy(board)
    if temp_board[action[0]][action[1]] is not EMPTY:
        return None
    temp_board[action[0]][action[1]] = player(board)
    return temp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    util = utility(board)
    if (util == 1):
        return X
    elif (util == -1):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # To check if the board is full
    board_full = False
    for rows in board:
        if all(tiles is not None for tiles in rows):
            board_full = True
        else:
            board_full = False
            break
    if board_full == True:
        return True

    # to check if there is a row of X or O
    for rows in board:
        if all(tiles is X for tiles in rows) or all(tiles is O for tiles in rows):
            return True

    # to check if there is column of X or O
    for i in range(0, 3):
        if all(board[j][i] is X for j in range(0, 3)) or (all(board[j][i] is O for j in range(0, 3))):
            return True

    # to check if there are X or O diagonally
    if all(board[i][i] is X for i in range(0, 3)) or all(board[i][i] is O for i in range(0, 3)):
        return True
    if all(board[2 - i][i] is X for i in range(0, 3)) or all (board[2 - i][i] is O for i in range(0,3)):
        return True

    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # to check if there is row of X or O
    for rows in board:
        if all(tiles is X for tiles in rows):
            return 1
        if all(tiles is O for tiles in rows):
            return -1

    # to check if there is column of X or O
    for i in range(0, 3):
        if all(board[j][i] is X for j in range(0, 3)):
            return 1
        if all(board[j][i] is O for j in range(0, 3)):
            return -1

    # to check if there are X or O diagonally
    if all(board[i][i] is X for i in range(0, 3)):
        return 1
    if all(board[i][i] is O for i in range(0, 3)):
        return -1
    if all(board[2 - i][i] is X for i in range(0, 3)):
        return 1
    if all(board[2 - i][i] is O for i in range(0, 3)):
        return -1


    # To check if the board is full, hence tied
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if game has completed
    if terminal(board):
        return None

    # first move if O is chosen for efficiency
    if board == initial_state():
        return (0,0)

    # to return max possible outcome
    def moveX(board):
        if terminal(board):
            return utility(board)
        v = -INFINTY
        for action in actions(board):
            v = max(v, moveO(result(board, action)))
        return v

    # to return min possible outcome
    def moveO(board):
        if terminal(board):
            return utility(board)
        v = INFINTY
        for action in actions(board):
            v = min(v, moveX(result(board, action)))
        return v

    turn = player(board)
    optimal_action = None

    # for X's turn
    if turn == X:
        v = -INFINTY
        for action in actions(board):
            value = moveO(result(board, action))
            if value > v:
                v = value
                optimal_action = action

    # if O's turn
    else:
        v = INFINTY
        for action in actions(board):
            value = moveX(result(board, action))
            if value < v:
                v = value
                optimal_action = action

    return optimal_action
