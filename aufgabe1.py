#%%
import random


def get_lotto():
    numbers = [x for x in range(1, 46)]

    for x in range(44, 38, -1):
        rand = random.randint(0, x)
        numbers[rand], numbers[x] = numbers[x], numbers[rand]

    return numbers[-6:]


stats = [0 for _ in range(46)]
for _ in range(1000000):
    one = get_lotto()
    for x in one:
        stats[x] = stats[x] + 1

print(stats[1:])
low = min(stats[1:])
high = max(stats[1:])
print(f"{low = }\t{high = }\n{high - low}")
