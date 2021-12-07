import math
import numpy as np

with open('input.txt') as f:
    positions = np.array(f.read().split(','), dtype=int)

distance = abs(positions-int(np.mean(positions)))  # distance to the (rounded) mean: fewest average nr of steps
fuel_cost = map(lambda d: math.comb(d+1, 2), distance)  # (distance+1 choose n) is the fuel cost
print(sum(fuel_cost))
