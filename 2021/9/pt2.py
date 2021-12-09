import numpy as np
from typing import List, Set, Tuple, AbstractSet
from functools import reduce

with open('input.txt') as file:
    grid = np.array([list(line) for line in file.read().split()], dtype=int)

basin_fields = grid != 9  # all values that are not 9 are part of a basin
basin_coords: List[Tuple[int, int]] = []  # Coordinate tuples of the basin fields
for i, part_of_basin in enumerate(basin_fields.flatten()):
    if part_of_basin:
        basin_coords.append((i % len(grid[0]), i // len(grid[0])))  # (row, col)


def grow_basin_from_coords(row: int, col: int) -> AbstractSet[Tuple[int, int]]:
    basin: Set[Tuple[int, int]] = set()
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            basin_coords.remove(field := (row + direction[0], col + direction[1]))
            basin.add(field)
        except ValueError:
            pass
    return reduce(set.__or__, [grow_basin_from_coords(*b) for b in basin], basin)


basins: List[AbstractSet[Tuple[int, int]]] = []  # list of all basins, represented as a set of coordinates
while not len(basin_coords) == 0:  # More basins left
    basins.append(grow_basin_from_coords(*(coords := basin_coords.pop())) | {coords})

print(reduce(int.__mul__, sorted(map(len, basins), reverse=True)[:3]))
