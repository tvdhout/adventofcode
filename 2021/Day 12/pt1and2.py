from collections import defaultdict
from typing import List

with open('input.txt') as file:
    lines = file.read().split()

connections = defaultdict(list)
for line in lines:
    start, stop = line.split('-')
    if stop != 'start' and start != 'end':
        connections[start].append(stop)
    start, stop = stop, start
    if stop != 'start' and start != 'end':
        connections[start].append(stop)

paths: List[List[str]] = []


def expand_path(path: List[str], small_cave_privilege: str = None):
    global paths
    for connects in connections[path[-1]]:
        if connects == 'end':
            paths.append(path + ['end'])
            continue
        if connects.islower() and connects in path:
            # part 2
            if small_cave_privilege is None or small_cave_privilege == connects and path.count(connects) < 2:
                expand_path(path + [connects], connects)
            # end part 2
            continue
        expand_path(path + [connects], small_cave_privilege)


expand_path(['start'])
print(len(paths))
