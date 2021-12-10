with open('input.txt') as file:
    lines = file.read().split()

errors = []
costs = {')': 3,
         ']': 57,
         '}': 1197,
         '>': 25137}

for line in lines:
    to_close = []
    for char in line:
        match char:
            case '(': to_close.append(')')
            case '[': to_close.append(']')
            case '{': to_close.append('}')
            case '<': to_close.append('>')
            case closing:  # Closing character
                if closing != to_close.pop():  # not the expected closing character
                    errors.append(closing)
                    break

print(sum([costs[e] for e in errors]))
