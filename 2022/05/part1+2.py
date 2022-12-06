import re

import numpy as np

PART2 = False
with open('input.txt') as file:
    crates, lines = file.read().split('\n\n')

# Parse crates
crates = np.array([list(line) for line in crates.split('\n')]).T[1::4].T[:-1].T.tolist()
crates = [[i for i in c if i != ' '] for c in crates]

# Parse instructions
instructions = re.findall(r'move (\d+) from (\d+) to (\d+)', lines)
instructions = list(map(lambda x: (int(x[0]), int(x[1])-1, int(x[2])-1), instructions))

for nr, fro, to in instructions:
    for i in range(nr):
        crates[to].insert(i if PART2 else 0, crates[fro].pop(0))

print(''.join([c[0] for c in crates]))
