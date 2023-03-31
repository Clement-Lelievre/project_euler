"""https://projecteuler.net/problem=628
A position in chess is an (orientated) arrangement of chess pieces placed on a chessboard of given size. 
In the following, we consider all positions in which pawns are placed on a

board in such a way, that there is a single pawn in every row and every column.

We call such a position an open position, if a rook, starting at the (empty) lower left corner and using only 
moves towards the right or upwards, can reach the upper right corner without moving onto any field occupied by a pawn.

Let f(n) be the number of open positions for a chessboard.
"""


def nb_open_positions(n_rows: int, n_cols: int):
    if n_cols == n_rows == 3:
        return 2
    if n_cols == 3 and n_rows == 2:
        return
