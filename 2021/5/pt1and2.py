import re
import numpy as np
from typing import List, Tuple

with open('input.txt') as f:
    lines = f.read().split('\n')

lines = np.array([re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in lines], dtype=int)
grid = np.zeros((lines.max()+1, lines.max()+1))

# Part 1: only horizontal or vertical lines
# mask = [line[0] == line[2] or line[1] == line[3] for line in lines]
# lines = lines[mask]


def get_line_coords(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
    coords = [(x1, y1)]
    diff_x = x2 - x1
    diff_y = y2 - y1
    n_steps = max(abs(diff_x), abs(diff_y))
    x_step = diff_x // n_steps
    y_step = diff_y // n_steps
    for _ in range(n_steps):
        x1 += x_step
        y1 += y_step
        coords.append((x1, y1))
    return coords


for line in lines:
    for coords in get_line_coords(*line):
        grid[coords] += 1

print(np.sum(grid > 1))
