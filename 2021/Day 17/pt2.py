target_x = range(48, 71)
target_y = range(-189, -147)

total_combinations = 0

# Lazy solution... may revisit
for _xv in range(target_x[-1]+1):
    for _yv in range(-190, 190):
        xv, yv = _xv, _yv
        x, y = 0, 0
        while x < target_x[-1] and y > target_y[0]:
            x += xv
            y += yv
            xv -= 1 if xv > 0 else -1 if xv < 0 else 0
            yv -= 1
            if x in target_x and y in target_y:
                total_combinations += 1
                break

print(total_combinations)
