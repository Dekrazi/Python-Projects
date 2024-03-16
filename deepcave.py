import random
import sys
import time


WIDTH = 70
PAUSE_AMOUNT = 0.3

print('Deep cave!')
print('Press ctrl + c to stop')

time.sleep(3)

left_side = 20
gap = 10

while True:
    right_side = WIDTH - gap - left_side
    print(('#' * left_side) + (' ' * gap) + ('#' * right_side))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    random_roll = random.randint(1, 6)

    if random_roll == 1 and left_side > 1:
        left_side -= 1
    elif random_roll == 2 and left_side + gap < WIDTH - 1:
        left_side += 1
    else:
        pass
