import re
import time

start = time.time()

ms = map(lambda x: list(map(int, x)), re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', open('input.txt').read()))

print(sum([(m[1] >= m[2] and m[0] <= m[3]) or
           (m[3] >= m[0] and m[2] <= m[1])
           for m in ms]))

print(time.time() - start)