from itertools import permutations
from pt1 import numbers, reduce, magnitude

highest_magnitude = 0
for combination in permutations(numbers, 2):
    reduction = reduce(str([eval(combination[0])] + [eval(combination[1])]))
    m = magnitude(eval(reduction))
    highest_magnitude = max(highest_magnitude, m)

print(highest_magnitude)
