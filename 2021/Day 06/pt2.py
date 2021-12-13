import numpy as np

with open('input.txt') as f:
    timers = np.array(f.read().split(','), dtype=int)

# Part 1 approach clearly doesn't scale... Trying something else
days_due_counts = {x: 0 for x in range(9)}
days_due, counts = np.unique(timers, return_counts=True)
days_due_counts.update({d: c for d, c in zip(days_due, counts)})

for _ in range(256):
    nr_due = days_due_counts[0]  # Number of lanternfish due today
    for i in range(8):
        days_due_counts[i] = days_due_counts[i+1]  # Everyone else is due one day less
    days_due_counts[6] += nr_due  # Lanternfish due today are again due in 7 days
    days_due_counts[8] = nr_due  # Lanternfish hatched today are due in 9 days

print(sum(days_due_counts.values()))
