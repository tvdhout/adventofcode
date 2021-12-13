import sys
import numpy as np

with open('input.txt') as f:
    numbers, *boards = f.read().split('\n\n')
numbers = list(map(int, numbers.split(',')))
boards = np.array([[row.split() for row in board.split('\n')] for board in boards], dtype=int)
mask = np.zeros_like(boards, dtype=bool)

for number in numbers:
    mask |= boards == number
    for board, called_mask in zip(boards, mask):
        for row in np.concatenate((called_mask, called_mask.T)):
            if all(row):
                print(sum(board[~called_mask]) * number)
                sys.exit(0)
