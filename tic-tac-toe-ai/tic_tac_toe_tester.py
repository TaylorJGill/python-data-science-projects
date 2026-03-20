"""Tests for the Tic Tac Toe implementation.

Run directly:  python tic_tac_toe_tester.py
With pytest:   pytest tic_tac_toe_tester.py
"""
from copy import deepcopy
from tic_tac_toe_board_and_judge import (
    IsSpaceFree, GetNumberOfChessPieces, IsBoardFull, IsBoardEmpty,
    UpdateBoard, Judge,
)
from ComputerPlayer import ComputerPlayer

# ── Test boards (Board k has k pieces placed) ─────────────────────────────────
Board0 = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
Board1 = [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
Board2 = [['O', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
Board3 = [['O', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
Board4 = [['O', ' ', 'O'], [' ', 'X', ' '], [' ', ' ', 'X']]
Board5 = [['O', 'X', 'O'], [' ', 'X', ' '], [' ', ' ', 'X']]
Board6 = [['O', 'X', 'O'], [' ', 'X', ' '], [' ', 'O', 'X']]
Board7 = [['O', 'X', 'O'], [' ', 'X', 'X'], [' ', 'O', 'X']]
Board8 = [['O', 'X', 'O'], ['O', 'X', 'X'], [' ', 'O', 'X']]
Board9 = [['O', 'X', 'O'], ['O', 'X', 'X'], ['X', 'O', 'X']]
boards = [Board0, Board1, Board2, Board3, Board4,
          Board5, Board6, Board7, Board8, Board9]


# ── IsSpaceFree ───────────────────────────────────────────────────────────────
def test_is_space_free():
    for i in range(3):
        for j in range(3):
            assert IsSpaceFree(deepcopy(Board0), i, j) is True

    for i in range(3):
        for j in range(3):
            assert IsSpaceFree(deepcopy(Board9), i, j) is False

    for i in range(-5, -1):
        for j in range(-5, -1):
            assert IsSpaceFree(deepcopy(Board0), i, j) is False


# ── GetNumberOfChessPieces ────────────────────────────────────────────────────
def test_get_number_of_chess_pieces():
    for k, board in enumerate(boards):
        assert GetNumberOfChessPieces(deepcopy(board)) == k


# ── IsBoardFull ───────────────────────────────────────────────────────────────
def test_is_board_full():
    assert IsBoardFull(Board9) is True
    for k in range(9):
        assert IsBoardFull(deepcopy(boards[k])) is False


# ── IsBoardEmpty ──────────────────────────────────────────────────────────────
def test_is_board_empty():
    assert IsBoardEmpty(Board0) is True
    for k in range(1, 10):
        assert IsBoardEmpty(deepcopy(boards[k])) is False


# ── UpdateBoard ───────────────────────────────────────────────────────────────
def test_update_board():
    for i in range(3):
        for j in range(3):
            temp = deepcopy(Board0)
            UpdateBoard(temp, 'X', (i, j))
            assert temp[i][j] == 'X'

            temp = deepcopy(Board0)
            UpdateBoard(temp, 'O', (i, j))
            assert temp[i][j] == 'O'


# ── ComputerPlayer (N=0, random) ──────────────────────────────────────────────
def test_computer_player_random():
    """N=0: returns a valid empty cell without modifying the board."""
    for k in range(1, 9):
        for tag in ('X', 'O'):
            board_k = deepcopy(boards[k])
            original = deepcopy(boards[k])
            i, j = ComputerPlayer(tag, board_k, N=0)
            assert i in [0, 1, 2] and j in [0, 1, 2]
            assert board_k[i][j] == ' '
            assert board_k == original


# ── ComputerPlayer (N=1, one-step lookahead) ──────────────────────────────────
def test_computer_player_lookahead():
    """N=1: wins when possible, otherwise blocks the opponent."""
    cases = [
        ('O', [['X', ' ', ' '], [' ', 'O', ' '], ['X', ' ', ' ']], [1, 0]),  # block col
        ('O', [['O', ' ', 'X'], [' ', ' ', ' '], ['X', ' ', ' ']], [1, 1]),  # take center
        ('O', [['X', ' ', ' '], [' ', 'X', ' '], ['O', ' ', ' ']], [2, 2]),  # block diagonal
        ('O', [['X', ' ', 'X'], [' ', 'X', ' '], ['O', ' ', 'O']], [2, 1]),  # win (row)
        ('X', [['O', ' ', 'X'], [' ', 'X', ' '], [' ', ' ', 'O']], [2, 0]),  # win (diagonal)
        ('X', [['O', 'X', ' '], [' ', 'X', ' '], [' ', ' ', 'O']], [2, 1]),  # win (col)
        ('X', [['X', 'O', ' '], ['X', ' ', ' '], [' ', ' ', 'O']], [2, 0]),  # win (col)
        ('X', [['X', ' ', 'X'], ['O', ' ', 'O'], [' ', ' ', ' ']], [0, 1]),  # win (row)
    ]
    for tag, board, expected in cases:
        choice = ComputerPlayer(tag, board, N=1)
        assert list(choice) == expected, (
            f"Tag={tag}, board={board}, expected {expected}, got {list(choice)}"
        )


# ── Judge ─────────────────────────────────────────────────────────────────────
def test_judge_in_progress():
    for k in range(9):
        assert Judge(boards[k]) == 0


def test_judge_tie():
    assert Judge(Board9) == 3


def test_judge_x_wins():
    x_wins = [
        [['X', 'X', 'X'], ['O', ' ', 'O'], [' ', ' ', ' ']],   # top row
        [[' ', ' ', ' '], ['X', 'X', 'X'], ['O', ' ', 'O']],   # middle row
        [[' ', ' ', ' '], ['O', ' ', 'O'], ['X', 'X', 'X']],   # bottom row
        [['X', 'O', ' '], ['X', ' ', 'O'], ['X', ' ', ' ']],   # left col
        [['O', 'X', ' '], [' ', 'X', 'O'], [' ', 'X', ' ']],   # middle col
        [['O', ' ', 'X'], [' ', ' ', 'X'], [' ', 'O', 'X']],   # right col
        [[' ', ' ', 'X'], ['O', 'X', 'O'], ['X', ' ', ' ']],   # diagonal
        [['X', ' ', ' '], ['O', 'X', 'O'], [' ', ' ', 'X']],   # anti-diagonal
        [['X', 'X', 'O'], ['X', 'O', 'O'], ['X', 'O', 'X']],   # full board, X wins
    ]
    for board in x_wins:
        assert Judge(board) == 1


def test_judge_o_wins():
    o_wins = [
        [['X', ' ', 'X'], [' ', ' ', ' '], ['O', 'O', 'O']],   # bottom row
        [['X', ' ', 'X'], ['O', 'O', 'O'], ['X', ' ', ' ']],   # middle row
        [['O', 'O', 'O'], ['X', ' ', ' '], ['X', ' ', 'X']],   # top row
        [['O', 'X', 'X'], ['O', ' ', ' '], ['O', ' ', 'X']],   # left col
        [['X', 'O', 'X'], [' ', 'O', ' '], [' ', 'O', 'X']],   # middle col
        [['X', 'X', 'O'], [' ', ' ', 'O'], ['X', ' ', 'O']],   # right col
        [['O', 'X', 'X'], [' ', 'O', ' '], ['X', ' ', 'O']],   # diagonal
        [['X', 'X', 'O'], [' ', 'O', ' '], ['O', ' ', 'X']],   # anti-diagonal
        [['X', 'X', 'O'], ['X', 'O', 'O'], ['O', 'X', 'X']],   # full board, O wins
    ]
    for board in o_wins:
        assert Judge(board) == 2


# ── Runner ────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    tests = [
        test_is_space_free,
        test_get_number_of_chess_pieces,
        test_is_board_full,
        test_is_board_empty,
        test_update_board,
        test_computer_player_random,
        test_computer_player_lookahead,
        test_judge_in_progress,
        test_judge_tie,
        test_judge_x_wins,
        test_judge_o_wins,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"  PASS  {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {test.__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed")
