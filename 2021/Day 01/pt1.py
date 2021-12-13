with open('input.txt') as f:
    numbers = [int(m) for m in f.read().split()]

increased = 0
current = numbers[0]
for i in range(1, len(numbers)):
    increased += current < (current := numbers[i])
print(increased)
