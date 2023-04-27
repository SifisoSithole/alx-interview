#!/usr/bin/python3
"""
Solution to the N queens problem
"""
import sys


def solve_N_queen(N):
    """
    Returns array of possible queen placements
    Parameters:
        N (int): Size of the board and the number of queens
    Return:
        Possible queen placements
    """
    column = set()
    positive_diagonal = set()
    negative_diagonal = set()
    solutions = []
    board = [["."] * N for i in range(N)]

    def backtrack(row):
        if row == N:
            for x in range(N):
                cor = []
                for y in range(N):
                    if board[x][y] == "Q":
                        cor.append(x)
                        cor.append(y)
                        solutions.append(cor)

        for c in range(N):
            if c in column:
                continue
            if row + c in positive_diagonal or row - c in negative_diagonal:
                continue

            column.add(c)
            positive_diagonal.add(row + c)
            negative_diagonal.add(row - c)
            board[row][c] = "Q"

            backtrack(row + 1)

            column.remove(c)
            positive_diagonal.remove(row + c)
            negative_diagonal.remove(row - c)
            board[row][c] = "."

    backtrack(0)
    return solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
N = sys.argv[1]
if N.isdigit():
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)
else:
    print("N must be a number")
    exit(1)
solutions = solve_N_queen(N)
i = 0
result = []
for solution in solutions:
    result.append(solution)
    i += 1
    if i == N:
        i = 0
        print(result)
        result = []
