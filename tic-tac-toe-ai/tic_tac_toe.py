import random
from ComputerPlayer import ComputerPlayer
from tic_tac_toe_board_and_judge import DrawBoard, UpdateBoard, IsSpaceFree, Judge


def HumanPlayer(Tag, Board, N=None):
    """Prompt the human player to choose a move.

    Parameters:
        Tag   : 'X' or 'O'
        Board : 3x3 nested list representing the game board
        N     : unused (kept for interface consistency with ComputerPlayer)

    Returns:
        (row, col) — a valid, unoccupied board position

    Notes:
        Board is NOT modified. Loops until valid input is received.
    """
    while True:
        try:
            row = int(input(f"Player {Tag}, enter row (0-2): "))
            col = int(input(f"Player {Tag}, enter column (0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue

            if not IsSpaceFree(Board, row, col):
                print("That spot is already taken. Try again.")
                continue

            return (row, col)

        except ValueError:
            print("Please enter numbers only (0, 1, or 2).")


def ShowOutcome(Outcome, NameX, NameO):
    """Print a message describing the current game outcome.

    Parameters:
        Outcome : integer from Judge (0=in progress, 1=X wins, 2=O wins, 3=tie)
        NameX   : display name for the X player
        NameO   : display name for the O player
    """
    if Outcome == 0:
        print("The game is still in progress.")
    elif Outcome == 1:
        print(f"PlayerX ({NameX}, X) wins!")
    elif Outcome == 2:
        print(f"PlayerO ({NameO}, O) wins!")
    elif Outcome == 3:
        print("It's a tie!")


def WhichPlayerGoesFirst(ComputerPlayer, HumanPlayer):
    """Randomly assign which player takes X (goes first).

    Returns:
        (PlayerX, PlayerO) — two player function objects
    """
    if random.randint(0, 1) == 0:
        print('Computer player goes first')
        PlayerX = ComputerPlayer
        PlayerO = HumanPlayer
    else:
        print('Human player goes first')
        PlayerO = ComputerPlayer
        PlayerX = HumanPlayer
    return PlayerX, PlayerO


def TicTacToeGame():
    """Run a single game of Tic Tac Toe (human vs. computer)."""
    print('Welcome to Tic Tac Toe')
    N = input('Set computer lookahead depth (0 = random, 1 = strategic): N=')
    try:
        N = int(N)
        if N < 0:
            print('N < 0, setting to 0')
            N = 0
        if N > 1:
            print('N > 1, setting to 1')
            N = 1 # lookahead only supports depth 0 (random) or 1 (strategic)
    except ValueError:
        print('Invalid input, setting N to 0')
        N = 0

    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)

    PlayerX, PlayerO = WhichPlayerGoesFirst(ComputerPlayer, HumanPlayer)
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__

    while True:
        choiceX = PlayerX('X', Board, N)
        UpdateBoard(Board, 'X', choiceX)
        DrawBoard(Board)
        outcome = Judge(Board)
        ShowOutcome(outcome, NameX, NameO)
        if outcome in (1, 2, 3):
            break

        choiceO = PlayerO('O', Board, N)
        UpdateBoard(Board, 'O', choiceO)
        DrawBoard(Board)
        outcome = Judge(Board)
        ShowOutcome(outcome, NameX, NameO)
        if outcome in (1, 2, 3):
            break


def PlayGame():
    """Play multiple rounds until the user quits."""
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print('Game over')


if __name__ == '__main__':
    PlayGame()
