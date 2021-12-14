from collections import defaultdict

with open('input.txt') as file:
    template, rules = file.read().split('\n\n')
    rules = [rule.split(' -> ') for rule in rules.split('\n')]
    rules = dict([(x, (x[0] + y, y + x[1])) for x, y in rules])

pair_counts = {pair: template.count(pair) for pair in rules.keys()}
for _ in range(40):
    new_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        new_counts[rules[pair][0]] += count
        new_counts[rules[pair][1]] += count
    pair_counts = new_counts

letter_counts = defaultdict(int)
for pair, count in pair_counts.items():
    letter_counts[pair[0]] += count  # count first letter of every pair
letter_counts[template[-1]] += 1  # Last character of the polymer is not counted above

s = sorted(letter_counts.values())
print(s[-1] - s[0])
