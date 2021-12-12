import numpy as np

with open('input.txt') as file:
    grid = np.array([list(col) for col in file.read().split()], dtype=int)

has_flashed_this_step = np.zeros_like(grid, dtype=bool)
nr_flashes = 0


def flash(row, col):
    global nr_flashes
    nr_flashes += 1
    has_flashed_this_step[row, col] = True
    grid[row, col] = 0
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        r, c = row+d[0], col+d[1]
        try:
            assert r >= 0 and c >= 0
            if not has_flashed_this_step[r, c]:
                grid[r, c] += 1
        except (IndexError, AssertionError):
            pass


for step in range(1, 10000000):  # 100 steps for pt 1.
    has_flashed_this_step = np.zeros_like(grid, dtype=bool)
    grid += 1
    while (to_flash := grid > 9).any():
        for coords in np.argwhere(to_flash):
            flash(*coords)
    if has_flashed_this_step.all():
        print(step, "wins pt. 2")
        break

print(f"Number of flashes: {nr_flashes}")
