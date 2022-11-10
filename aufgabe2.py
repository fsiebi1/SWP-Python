#%%
import random
from typing import List, Tuple

import numpy as np

MAX = int(10e5)
PROZENT = MAX // 100

REAL = {
    "high-card": 50.1177,
    "pair": 42.22569,
    "two-pairs": 4.7539,
    "tripple": 2.21128,
    "straight": 0.3925,
    "flush": 0.1965,
    "house": 0.1441,
    "quads": 0.024,
    "straight flush": 0.0014,
    "royal flush": 0.0002,
}


def make_dict():
    result = {
        "high-card": 0,
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
    return result


def get_lotto(anz: int) -> List[int]:
    numbers = [x for x in range(52)]

    for x in range(51, 51 - anz, -1):
        rand = random.randint(0, x)
        numbers[rand], numbers[x] = numbers[x], numbers[rand]

    return numbers[-anz:]


def make_cards(numbers: List[int]) -> List[Tuple[int, int]]:
    liste = []
    for n in numbers:
        liste.append((n % 13, n // 13))

    liste.sort()
    return liste


def get_anz_same(cards: List[Tuple[int, int]], ort: int) -> int:
    anz = np.zeros(13)
    for t in cards:
        anz[t[ort]] = anz[t[ort]] + 1

    return int(anz.max())


def check_straight(cards: List[Tuple[int, int]]) -> bool:
    last = cards[0][0] - 1
    for c in cards:
        if not c[0] == last + 1:
            return False

        last = c[0]
    return True


def check_straight_double(cards: List[Tuple[int, int]]) -> bool:
    a = check_straight(cards)
    if cards[0][0] == 0:
        cards[0] = (13, cards[0][1])
        cards.sort()
        a = a or check_straight(cards)

    return a


def anz_zahlen(cards: List[Tuple[int, int]]) -> int:
    b = []
    for c in cards:
        b.append(c[0])

    return len(np.unique(b))


def check(cards: List[Tuple[int, int]]):
    number = get_anz_same(cards, 0)
    color = get_anz_same(cards, 1)

    if number == 4:
        return "quads"

    straight = check_straight_double(cards)
    if color == 5 and straight:
        if cards[4][0] == 13:
            return "royal flush"
        return "straight flush"

    if color == 5:
        return "flush"

    if straight:
        return "straight"

    anz_z = anz_zahlen(cards)
    if anz_z == 2:
        return "house"

    if number == 3:
        return "tripple"

    if anz_z == 3:
        return "two-pairs"

    if number == 2:
        return "pair"

    return "high-card"


def _main():
    result = make_dict()

    for x in range(MAX):
        arr = get_lotto(5)
        numbers = make_cards(arr)
        what = check(numbers)
        result[what] += 1

    for k in result.keys():
        print(f"{k:14}: {result[k] / PROZENT:8.5f} %\t{REAL[k]:8.5f} %")


if __name__ == "__main__":
    _main()
