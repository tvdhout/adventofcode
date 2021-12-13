import numpy as np

with open('input.txt') as f:
    lines = f.read().split('\n')

_, digits_output = np.array([line.split('|') for line in lines]).T
digits_output = list(np.array([pat.strip().split() for pat in digits_output]).flatten())
digits_output = list(map(len, digits_output))

occurrence = 0
for val in [2, 3, 4, 7]:
    occurrence += digits_output.count(val)

print(occurrence)
