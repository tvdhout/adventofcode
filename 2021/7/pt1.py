import numpy as np

with open('input.txt') as f:
    positions = np.array(f.read().split(','), dtype=int)

print(sum(abs(positions-int(np.median(positions)))))  # Summed distance to the median (fewest total steps)
