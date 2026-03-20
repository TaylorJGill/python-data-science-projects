def DrawBoard(Board):
    """Print the 3x3 game board to the console.

    Example output:
        O|X|X
        -+-+-
        X|X|O
        -+-+-
        O|O|X
    """
    for i in range(3):
        print(f"{Board[i][0]}|{Board[i][1]}|{Board[i][2]}")
        if i < 2:
            print("-+-+-")


def IsSpaceFree(Board, i, j):
    """Return True if Board[i][j] is empty (' '), False otherwise.

    Returns False for out-of-range indices (valid range: 0–2).
    """
    if i < 0 or i > 2 or j < 0 or j > 2:
        return False
    return Board[i][j] == ' '


def GetNumberOfChessPieces(Board):
    """Return the total number of 'X' and 'O' pieces on the board."""
    count = 0
    for i in range(3):
        for j in range(3):
            if Board[i][j] != ' ':
                count += 1
    return count


def IsBoardFull(Board):
    """Return True if all 9 squares are occupied."""
    return GetNumberOfChessPieces(Board) == 9


def IsBoardEmpty(Board):
    """Return True if the board has no pieces placed."""
    return GetNumberOfChessPieces(Board) == 0


def UpdateBoard(Board, Tag, Choice):
    """Place Tag ('X' or 'O') at position Choice = (row, col) on Board."""
    r, c = Choice
    Board[r][c] = Tag


def Judge(Board):
    """Determine the current game outcome.

    Returns:
        0 — game in progress
        1 — X wins
        2 — O wins
        3 — tie (board full, no winner)
    """
    def line_winner(a, b, c):
        if a == b == c and a in ('X', 'O'):
            return a
        return None

    for i in range(3):
        w = line_winner(Board[i][0], Board[i][1], Board[i][2])
        if w == 'X': return 1
        if w == 'O': return 2

        w = line_winner(Board[0][i], Board[1][i], Board[2][i])
        if w == 'X': return 1
        if w == 'O': return 2

    w = line_winner(Board[0][0], Board[1][1], Board[2][2])
    if w == 'X': return 1
    if w == 'O': return 2

    w = line_winner(Board[0][2], Board[1][1], Board[2][0])
    if w == 'X': return 1
    if w == 'O': return 2

    if GetNumberOfChessPieces(Board) == 9:
        return 3
    return 0
