with open('input.txt') as f:
    numbers = [int(m) for m in f.read().split()]

increased = 0
current = sum(numbers[:3])
for i in range(1, len(numbers)-2):
    increased += current < (current := sum(numbers[i:i+3]))
print(increased)
