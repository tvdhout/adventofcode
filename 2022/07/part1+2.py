from typing import Iterator

with open('input.txt') as file:
    lines: Iterator[str] = iter(file.read().split('\n')[1:])


def build_tree(tree: dict[str, dict | int] = None) -> dict[str, dict | int]:
    tree = tree or {}
    while line := next(lines, False):
        if line == '$ ls':
            continue
        if line == '$ cd ..':
            return tree or {}
        if line.startswith('$ cd '):
            tree[line.split()[-1]] = build_tree(tree.get(line.split()[-1], None))
            continue
        a, b = line.split()
        if a == 'dir' and b not in tree:
            tree[b] = {}
        else:
            tree[b] = int(a)
    return tree


tree = {'/': build_tree()}
sum_sized_under_100k = 0
sizes = []


def compute_size(tree) -> int:
    global sum_sized_under_100k
    total = sum([tree[item] if type(tree[item]) == int else compute_size(tree[item]) for item in tree])
    if total <= 100_000:
        sum_sized_under_100k += total
    sizes.append(total)
    return total


root_size = compute_size(tree)
print('part 1:,', sum_sized_under_100k)

space_to_free = 30000000 - (70000000 - root_size)
for size in sorted(sizes):
    if size >= space_to_free:
        print('part 2:', size)
        break
