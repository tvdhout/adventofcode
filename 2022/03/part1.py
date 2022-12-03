import string

priorities = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

with open('input.txt') as file:
    rucksacks = file.read().split()

points = sum([priorities[(set(r[len(r)//2:]) & set(r[:len(r)//2])).pop()] for r in rucksacks])
print(points)
