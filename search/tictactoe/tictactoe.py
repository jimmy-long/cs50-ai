"""
Tic Tac Toe Player
"""

import math

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if sum(1 for row in board for val in row if val is not None) % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spaces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_spaces.append((i, j))
    return empty_spaces


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[i])):
            new_row.append(board[i][j] if not (i, j) == action else player(board))
        new_board.append(new_row)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    size = len(board)
    scores = [0] * (size * 2 + 2)

    for i in range(len(board)):
        for j in range(len(board[i])):
            points = 1 if board[i][j] == X else -1 if board[i][j] == O else 0
            scores[i] += points
            scores[j + len(board)] += points
            if i == j: scores[-2] += points
            if i == size - j - 1: scores[-1] += points

    for score in scores:
        if score == size:
            return X
        elif score == -size:
            return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: return True
    return True if sum(1 for row in board for val in row if val is not None) == len(board)**2 else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner is None: return 0
    return 1 if game_winner == X else -1 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return

    if player(board) == X:
        return max_value(board)[1]
    return min_value(board)[1]

def min_value(board):
    """
    Returns a tuple of the form (value, action) that the min player would
    take given the current board state.
    Keep in mind, that action is, itself, a tuple of the form (i, j).
    """
    if terminal(board):
        return (utility(board), None)

    # This the tuple we will end up returning. We should think of it as
    # result = (value, action)
    value_action = (float('inf'), None)
    for action in actions(board):
        max_result = max_value(result(board, action))
        if max_result[0] < value_action[0]:
            value_action = (max_result[0], action)

    return value_action


def max_value(board):
    """
    Returns a tuple of the form (value, action) that the max player would
    take given the current board state.
    Keep in mind, that action is, itself, a tuple of the form (i, j).
    """
    if terminal(board):
        return (utility(board), None)

    value_action = (float('-inf'), None)
    for action in actions(board):
        min_result = min_value(result(board, action))
        if min_result[0] > value_action[0]:
            value_action = (min_result[0], action)

    return value_action