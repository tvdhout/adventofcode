import numpy as np

with open('input.txt') as file:
    grid = np.asarray([list(row) for row in file.read().split()], dtype=int)

is_visible = np.zeros_like(grid, dtype=bool)

for n_rot in range(4):
    view = np.rot90(grid, k=n_rot)
    is_visible_tmp = []
    tallest = np.array([-1] * len(grid))
    for row in view:
        is_visible_tmp.append(row > tallest)
        tallest = np.amax(np.array([tallest, row]), axis=0)
    is_visible |= np.rot90(is_visible_tmp, k=4 - n_rot)

print(np.sum(is_visible))
