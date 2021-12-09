import numpy as np
from typing import List, Set, Tuple, AbstractSet
from functools import reduce
from PIL import Image
from colormap import colormap

with open('input.txt') as file:
    grid = np.array([list(line) for line in file.read().split()], dtype=int)

basin_fields = grid != 9  # all values that are not 9 are part of a basin
basin_coords: List[Tuple[int, int]] = []  # Coordinate tuples of the basin fields
for i, part_of_basin in enumerate(basin_fields.flatten()):
    if part_of_basin:
        basin_coords.append((i // len(grid[0]), i % len(grid[0])))  # (row, col)

image_array = np.zeros((100, 100), dtype=int) + (0.30 * basin_fields)
frames = [Image.fromarray(colormap(np.kron(image_array, np.ones((5, 5))), bytes=True))]


def take_image():
    frames.append(Image.fromarray(colormap(np.kron(image_array, np.ones((5, 5))), bytes=True)))


def grow_basin_from_coords(row: int, col: int) -> AbstractSet[Tuple[int, int]]:
    """
    Recusively grow the basin by looking at neighboring fields that are still in the basin_coords list.
    :param row: row coordinate
    :param col: column coordinate
    :return:
    """
    basin: Set[Tuple[int, int]] = set()
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            basin_coords.remove(field := (row + direction[0], col + direction[1]))
            basin.add(field)
            image_array[field[0], field[1]] += 0.3  # Change color to silver in animation
            take_image()
        except ValueError:
            pass
    return reduce(set.__or__, [grow_basin_from_coords(*coord) for coord in basin], basin)


basins: List[AbstractSet[Tuple[int, int]]] = []  # list of all basins, represented as a set of coordinates
while not len(basin_coords) == 0:  # More basins left
    b = grow_basin_from_coords(*(coords := basin_coords.pop())) | {coords}
    image_array[coords[0], coords[1]] += 0.33
    for coords in b:  # Change color to gold in animation
        image_array[coords[0], coords[1]] += 0.3
    take_image()
    basins.append(b)


biggest_three = sorted(basins, key=len, reverse=True)[:3]
# Turn three biggest basins red in animation
for basin in biggest_three:
    for coords in basin:
        image_array[coords[0], coords[1]] = 1
    take_image()

# Save GIF
frames[0].save('basin_animation.gif', save_all=True, append_images=frames[1:], optimize=False, duration=1, loop=1)

# multiply the lengths for the puzzle's answer
print(reduce(int.__mul__, map(len, biggest_three)))
