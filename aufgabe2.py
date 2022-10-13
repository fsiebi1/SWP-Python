#%%
import random
from typing import List

result = {
    "pair": 0,
    "two-pairs": 0,
    "tripple": 0,
    "straight": 0,
    "flush": 0,
    "house": 0,
    "quads": 0,
    "straight flush": 0,
    "royal flush": 0,
}


def get_lotto(anz: int) -> List[int]:
    numbers = [x for x in range(52)]

    for x in range(51, 51 - anz, -1):
        rand = random.randint(0, x)
        numbers[rand], numbers[x] = numbers[x], numbers[rand]

    return numbers[-anz:]


if __name__ == "__main__":
    for x in range(100000):
        arr = get_lotto(5)
