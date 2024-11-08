#!/usr/bin/env python3
"""
N Queens Problem using Backtracking
"""

import sys

def queens(chessBoard, row, n, resolve):
    """
    Args:
        chessboard (list)
        row (int)
        n (int)
        resolve (list)

    Returns:
        resolve (list)
    """
    if n == len(chessBoard):
        resolve.append(extract(chessBoard))
        return resolve
    
    for col in range(len(chessBoard)):
        if chessBoard[row][col] == -1:
            demo = copyBoard(chessBoard)
            demo[row][col] = 1
            cancel(demo, row, col)
            resolve = queens(demo, row + 1, n + 1, resolve)
        return resolve

def cancel(chessBoard, row, col):
    """
    Cancels the current row and column in the chessboard
    Args:
     chessBoard (list)
     row (int)
     col (int)
    """
    length = len(chessBoard)
    """Cancel forward positions"""
    for c in range(col + 1, length):
        chessBoard[row][c] = 0
    """Cancel Backward positions"""
    for c in range(col - 1, -1, -1):
        chessBoard[row][c] = 0
    """Cancel down positions"""
    for r in range(row + 1, length):
        chessBoard[r][col] = 0
    """Cancel up positions"""
    for r in range(row - 1, -1, -1):
        chessBoard[r][col] = 0
    """Cancel right downward diagonal positions"""
    c = col + 1
    for r in range(row + 1, length):
        if c >= length:
            break
        chessBoard[r][c] = 0
        c += 1
    """Cancel left upward diagonal positions"""
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1
    """Cancel right upward diagonal positions"""
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= length:
            break
        chessBoard[r][c] = 0
        c += 1
    """Cancel left downward diagonal positions"""
    c = col - 1
    for r in range(row + 1, length):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1

def chessBoard(N):
    """Create a board of size N * N"""
    chessBoard = []

    """rows"""
    for row in range(N):
        chessBoard.append([])

    """columns"""
    for row in chessBoard:
        for n in range(N):
            row.append(-1)

    return chessBoard

def copyBoard(chessBoard):
    """Makes a copy of the chessboard"""
    if type(chessBoard) == list:
        """recursively copy nested lists"""
        return list(map(copyBoard, chessBoard))
    return chessBoard


def extract(chessBoard):
    """Extracts the solutions from the chessboard"""
    outcome = []
    for row in range(len(chessBoard)):
        for col in range(len(chessBoard)):
            if chessBoard[row][col] == 1:
                outcome.append((row, col))
                break
    return outcome

def execute():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isnumeric() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess = chessBoard(int(sys.argv[1]))
    result = queens(chess, 0, 0, [])
    for row in result:
        print(row)


if __name__ == "__main__":
    execute()
