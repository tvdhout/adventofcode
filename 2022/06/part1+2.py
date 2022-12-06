with open('input.txt') as file:
    stream = file.read()

nr_unique = 4  # 14 for part 2
for i in range(len(stream) - nr_unique):
    if len(set(stream[i:i + nr_unique])) == nr_unique:
        print(i + nr_unique)
        break
