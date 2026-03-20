# Tic Tac Toe AI

A command-line Tic Tac Toe game with a configurable computer opponent. The AI supports two difficulty modes and includes a full test suite.

---

## Files

| File | Description |
|------|-------------|
| `tic_tac_toe.py` | Main game loop — run this to play |
| `ComputerPlayer.py` | AI player logic |
| `tic_tac_toe_board_and_judge.py` | Board rendering, move validation, and win detection |
| `tic_tac_toe_tester.py` | Test suite |

---

## How to Play

```bash
python tic_tac_toe.py
```

You'll be prompted to set the computer's lookahead depth:

- **N=0** — Random play (picks any available square)
- **N=1** — Strategic play (wins when possible, blocks opponent, prefers center and corners)

The game randomly assigns who plays X (goes first). Enter row and column as integers 0–2 when prompted.

---

## AI Strategy (N=1)

The computer evaluates moves in this priority order:

1. **Win** — take any move that wins the game immediately
2. **Block** — prevent the opponent from winning on their next move
3. **Center** — take position (1, 1) if available
4. **Corner** — take any available corner
5. **Any** — take the first remaining open square

---

## Running the Tests

With pytest:
```bash
pytest tic_tac_toe_tester.py
```

Or directly:
```bash
python tic_tac_toe_tester.py
```

The test suite covers board utilities, win detection (all rows, columns, and diagonals), AI move selection for both N=0 and N=1, and edge cases including full/empty boards and out-of-bounds inputs.

---

## Requirements

Python 3.x — no external dependencies.
