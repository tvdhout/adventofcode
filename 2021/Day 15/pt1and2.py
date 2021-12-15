import numpy as np

with open('input.txt') as file:
    grid = np.array([list(row) for row in file.read().split('\n')], dtype=int)

# part 2
risk = np.tile(grid, (5, 5))
for i in range(1, 5):
    risk[i * len(grid):, :] += 1
    risk[:, i * len(grid):] += 1
risk[risk > 9] -= 9
# end part 2

dist = np.ma.MaskedArray(np.ones_like(risk) * np.inf, fill_value=np.inf)
dist[0, 0] = 0
dist.mask = np.zeros_like(risk)

while not dist.mask.all():
    u = np.unravel_index(np.argmin(dist), dist.shape)
    for d in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        neighbor = (u[0] + d[0], u[1] + d[1])
        try:
            assert neighbor[0] >= 0 and neighbor[1] >= 0
            if not dist.mask[neighbor]:
                if (new_dist := risk[neighbor] + dist[u]) < dist[neighbor]:
                    dist[neighbor] = new_dist
        except (IndexError, AssertionError):
            continue
    dist.mask[u] = True

print(np.array(dist, dtype=int)[-1, -1])
