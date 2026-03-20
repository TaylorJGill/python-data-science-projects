import random
import copy
from tic_tac_toe_board_and_judge import IsBoardEmpty, IsSpaceFree, Judge


def ComputerPlayer(Tag, Board, N):
    """Choose a move for the computer player.

    Parameters:
        Tag   : 'X' or 'O' — which piece this player uses
        Board : 3x3 nested list representing the game board
        N     : lookahead depth — 0 for random play, 1 for one-step-ahead strategy

    Returns:
        (row, col) — the chosen move; 0 <= row, col <= 2

    Notes:
        Board is NOT modified.
        N=1 strategy: win if possible, otherwise block opponent, then prefer
        center > corners > any remaining space.
    """
    if N == 0:
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if IsSpaceFree(Board, r, c):
                return (r, c)

    me = Tag
    opp = 'O' if Tag == 'X' else 'X'

    if IsBoardEmpty(Board):
        return (0, 0)

    empties = [(i, j) for i in range(3) for j in range(3) if IsSpaceFree(Board, i, j)]

    # Win if possible
    for (i, j) in empties:
        B = copy.deepcopy(Board)
        B[i][j] = me
        outcome = Judge(B)
        if (me == 'X' and outcome == 1) or (me == 'O' and outcome == 2):
            return (i, j)

    # Block opponent's winning move
    for (i, j) in empties:
        B = copy.deepcopy(Board)
        B[i][j] = opp
        outcome = Judge(B)
        if (opp == 'X' and outcome == 1) or (opp == 'O' and outcome == 2):
            return (i, j)

    # Take center
    if IsSpaceFree(Board, 1, 1):
        return (1, 1)

    # Take a corner
    for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if IsSpaceFree(Board, *corner):
            return corner

    return empties[0]
