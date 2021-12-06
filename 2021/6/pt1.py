import numpy as np

with open('input.txt') as f:
    timers = np.array(f.read().split(','), dtype=int)

for _ in range(80):
    timers -= 1
    timers[(hatched := timers == -1)] = 6
    timers = np.insert(timers, 0, [8]*sum(hatched))

print(len(timers))
