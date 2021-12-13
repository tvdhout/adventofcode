with open('input.txt') as f:
    rows = f.read().split('\n')

depth = 0
position = 0
for r in rows:
    operation, value = r.split()
    value = int(value)
    if operation == 'forward':
        position += value
    else:
        depth += value if operation == 'down' else -value

print(depth * position)
