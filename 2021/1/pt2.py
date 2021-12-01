with open('input.txt') as f:
    numbers = [int(m) for m in f.read().split()]

increased = 0
current = 1e100
for i in range(len(numbers)-2):
    increased += current < (current := sum(numbers[i:i+3]))
print(increased)
