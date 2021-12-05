import sys
import numpy as np

with open('input.txt') as f:
    numbers, *boards = f.read().split('\n\n')
numbers = list(map(int, numbers.split(',')))
boards = np.array([[row.split() for row in board.split('\n')] for board in boards], dtype=int)
mask = np.zeros_like(boards, dtype=bool)
playing = np.ones(len(boards), dtype=bool)

for number in numbers:
    mask |= boards == number
    for i, (board, called_mask) in enumerate(zip(boards, mask)):
        if not playing[i]:
            continue
        for row in np.concatenate((called_mask, called_mask.T)):
            if all(row):
                playing[i] = False
                if all(~playing):
                    print(sum(board[~called_mask]) * number)
                    sys.exit(0)
