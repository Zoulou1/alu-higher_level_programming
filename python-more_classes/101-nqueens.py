#!/usr/bin/python3
"""
This module solves the N queens puzzle.

The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard.
"""

import sys

def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)

def print_invalid_number_message_and_exit(message):
    """Prints the invalid number message and exits with status 1."""
    print(message)
    sys.exit(1)

def is_valid(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board=[], row=0):
    """Recursively solves the N queens puzzle."""
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board.append(col)
            solve_nqueens(N, board, row + 1)
            board.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_invalid_number_message_and_exit("N must be a number")
    if N < 4:
        print_invalid_number_message_and_exit("N must be at least 4")
    solve_nqueens(N)
