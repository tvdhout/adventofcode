target_y = range(-189, -147)

# If the probe is shot upwards with a velocity of 10 from y=0, the next time it hits y=0 on its downward projection
# the velocity will be -10, and -11 after that step. the higher the velocity the higher the max y position. The max
# velocity on the downward projection without overshooting the target is the negative of the lowest coord in the target
# So the upwards velocity should be the positive value -1 (to compensate for the y-=1 at y=0 on the downward path)
yv = abs(target_y[0]) - 1
print((yv ** 2 + yv) // 2)  # Max y
