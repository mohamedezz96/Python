# Tic-Tac-Toe Game

This is a simple program that allows you to play Tic-Tac-Toe against the computer. The game follows the following assumptions and rules:

- The computer plays with 'X'.
- You (the user) play with 'O'.
- The first move belongs to the computer, which is always placed in the middle of the board.
- All the squares are numbered from 1 to 9, row by row.
- The user inputs their move by entering the number of the square they choose.
- The number must be valid: an integer between 1 and 9, and the square cannot be already occupied.
- After each move, the program checks if the game is over, resulting in one of the following verdicts: the game should continue, the game ends with a tie, you win, or the computer wins.
- The computer's moves are chosen randomly, without any artificial intelligence.

## Example Session

+---+---+---+
| | | |
| 1 | 2 | 3 |
| | | |
+---+---+---+
| | | |
| 4 | X | 6 |
| | | |
+---+---+---+
| | | |
| 7 | 8 | 9 |
| | | |
+---+---+---+

Enter your move: 1
+---+---+---+
| | | |
| O | 2 | 3 |
| | | |
+---+---+---+
| | | |
| 4 | X | 6 |
| | | |
+---+---+---+
| | | |
| 7 | 8 | 9 |
| | | |
+---+---+---+

+---+---+---+
| | | |
| O | X | 3 |
| | | |
+---+---+---+
| | | |
| 4 | X | 6 |
| | | |
+---+---+---+
| | | |
| 7 | 8 | 9 |
| | | |
+---+---+---+

Enter your move: 8
+---+---+---+
| | | |
| O | X | 3 |
| | | |
+---+---+---+
| | | |
| 4 | X | 6 |
| | | |
+---+---+---+
| | | |
| 7 | O | 9 |
| | | |
+---+---+---+

+---+---+---+
| | | |
| O | X | 3 |
| | | |
+---+---+---+
| | | |
| 4 | X | X |
| | | |
+---+---+---+
| | | |
| 7 | O | 9 |
| | | |
+---+---+---+

Enter your move: 4
+---+---+---+
| | | |
| O | X | 3 |
| | | |
+---+---+---+
| | | |
| O | X | X |
| | | |
+---+---+---+
| | | |
| 7 | O | 9 |
| | | |
+---+---+---+

+---+---+---+
| | | |
| O | X | X |
| | | |
+---+---+---+
| | | |
| O | X | X |
| | | |
+---+---+---+
| | | |
| 7 | O | 9 |
| | | |
+---+---+---+

Enter your move: 7
+---+---+---+
| | | |
| O | X | X |
| | | |
+---+---+---+
| | | |
| O | X | X |
| | | |
+---+---+---+
| | | |
| O | O | 9 |
| | | |
+---+---+---+

Game over. You win!
