import re

with open('input.txt') as file:
    lines = file.read()

lines = re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', lines)
lines = map(lambda x: list(map(int, x)), lines)

total = sum([((line[0] <= line[2] and line[1] >= line[3]) or
              line[0] >= line[2] and line[1] <= line[3]) for line in lines])

print(total)
