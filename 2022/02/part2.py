shape_points = {'A': 1, 'B': 2, 'C': 3}
outcome_points = {'X': 0, 'Y': 3, 'Z': 6}
shapes = 'ABC'

with open('input.txt') as file:
    pairs = [pair.split() for pair in file.read().split('\n')]

points = sum([outcome_points[b] +
              shape_points[shapes[(shapes.index(a) + {'X': -1, 'Y': 0, 'Z': 1}[b]) % 3]]
              for a, b in pairs])

print(points)
