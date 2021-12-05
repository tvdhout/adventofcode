import numpy as np

with open('input.txt') as f:
    rows = np.array(f.read().split('\n'))
    grid = np.array([list(r) for r in rows]).astype(int)

mask_oxygen = np.ones(len(rows), dtype=bool)
mask_co2 = np.ones(len(rows), dtype=bool)
for col in grid.T:
    if sum(mask_oxygen) > 1:
        mask_oxygen &= col == int(sum(col[mask_oxygen]) >= len(col[mask_oxygen])/2)
    if sum(mask_co2) > 1:
        mask_co2 &= col == int(sum(col[mask_co2]) < len(col[mask_co2])/2)

life_support_rating = int(rows[mask_oxygen][0], 2) * int(rows[mask_co2][0], 2)
print(life_support_rating)
