import string

priorities = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

with open('input.txt') as file:
    rucksacks = file.read().split()

groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]

points = sum([priorities[(set(r[0]) & set(r[1]) & set(r[2])).pop()] for r in groups])

print(points)