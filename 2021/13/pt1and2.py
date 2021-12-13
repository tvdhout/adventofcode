import numpy as np

with open('input.txt') as file:
    dots, folds = file.read().split('\n\n')

folds = [(int('x' in line), int(line.rsplit('=', 1)[-1])) for line in folds.split('\n')]  # [(axis, index), ...]
dots = np.array([line.split(',')[::-1] for line in dots.split()], dtype=int)  # [[row, col], ...]

paper = np.zeros(dots.T.max(axis=1) + 1, dtype=bool)
paper[dots.T[0], dots.T[1]] = True

for ax, fold_point in folds:
    paper, _, to_fold = np.split(paper, [fold_point, fold_point + 1], axis=ax)
    flipped = np.flip(to_fold, axis=ax)
    slices = [slice(None)] * 2
    slices[ax] = slice(paper.shape[ax]-flipped.shape[ax], None)
    paper[tuple(slices)] |= flipped
    # break  # part one

print(paper.sum())
# Part two:
for row in paper:
    print(' '.join(row.astype(str)).replace('True', '#').replace('False', '.'))
