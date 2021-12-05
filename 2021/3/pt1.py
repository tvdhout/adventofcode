import numpy as np

with open('input.txt') as f:
    rows = f.read().split('\n')
    grid = np.array([list(r) for r in rows]).astype(int)

gamma_bin = ''
eps_bin = ''
for col in grid.T:
    gamma_bin += str(one_or_zero := int(sum(col) > len(col)//2))
    eps_bin += str(abs(one_or_zero-1))

power_consumption = int(gamma_bin, 2) * int(eps_bin, 2)
print(power_consumption)
