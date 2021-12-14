from collections import Counter

with open('input.txt') as file:
    template, rules = file.read().split('\n\n')
    rules = [rule.split(' -> ') for rule in rules.split('\n')]
    rules = dict([(x, x[0] + y + x[1]) for x, y in rules])

polymer = template
for _ in range(10):
    pairs = list(map(''.join, zip(polymer[:-1], polymer[1:])))
    polymer = pairs[0][0]
    for pair in pairs:
        polymer += rules.get(pair, pair)[1:]

counts = Counter(polymer).most_common()
print(counts[0][1] - counts[-1][1])
