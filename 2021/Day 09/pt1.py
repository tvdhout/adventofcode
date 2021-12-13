import numpy as np

with open('input.txt') as file:
    grid = np.array([list(line) for line in file.read().split()], dtype=int)

height_map = np.empty((4, *grid.shape), dtype=bool)
for nr_rotations in range(4):
    rotated = np.rot90(grid, k=nr_rotations)
    smaller = np.empty(grid.shape, dtype=bool)
    smaller[0] = np.array([True]*len(grid))
    for idx in range(1, len(rotated)):
        smaller[idx] = (rotated[idx] - rotated[idx-1]) < 0
    smaller = np.rot90(smaller, k=4-nr_rotations)
    height_map[nr_rotations] = smaller

low_points = grid[height_map.sum(axis=0) == 4]
answer = sum(low_points) + len(low_points)
print(answer)
