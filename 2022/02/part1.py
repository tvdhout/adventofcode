wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
translation = {'X': 'A', 'Y': 'B', 'Z': 'C'}
shape_points = {'X': 1, 'Y': 2, 'Z': 3}

with open('input.txt') as file:
    pairs = [pair.split() for pair in file.read().split('\n')]

points = 0
for a, b in pairs:
    points += shape_points[b]
    if a == translation[b]:
        points += 3
    elif wins[a] == b:
        points += 6

print(points)
