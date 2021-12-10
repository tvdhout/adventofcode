with open('input.txt') as file:
    lines = file.read().split()

scores = []
costs = {')': 1,
         ']': 2,
         '}': 3,
         '>': 4}

for line in lines:
    to_close = []
    score = 0
    for char in line:
        match char:
            case '(': to_close.append(')')
            case '[': to_close.append(']')
            case '{': to_close.append('}')
            case '<': to_close.append('>')
            case closing:  # Closing character
                if closing != to_close.pop():  # not the expected closing character
                    break  # Corrupted line
    else:
        for closing in to_close[::-1]:
            score *= 5
            score += costs[closing]
        scores.append(score)

print(sorted(scores)[len(scores)//2])
