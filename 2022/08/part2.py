import numpy as np

with open('input.txt') as file:
    grid = np.asarray([list(row) for row in file.read().split()], dtype=int)

scenic_score = np.ones_like(grid, dtype=int)

for n_rot in range(4):
    dimension_score = np.zeros_like(grid, dtype=int)
    view = np.rot90(grid, k=n_rot)
    for i, row in enumerate(view):
        looking = np.ones_like(row, dtype=bool)
        for j in range(i - 1, -1, -1):
            dimension_score[i] += looking
            looking &= row > view[j]
    scenic_score *= np.rot90(dimension_score, k=4 - n_rot)

print(np.max(scenic_score))
