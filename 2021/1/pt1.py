with open('input.txt') as f:
    increased = 0
    curr = '0'
    for measurement in f.read().split():
        increased += curr < (curr := measurement)
print(increased)
