#%%

from tools import Sign
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from api_client import get_stats, create_ifn_exist, add_value, use_DSGVO


def get_name_mode():
    print("Hello Player!")
    print("So you want to play: ROCK PAPER SCISSORS SPOCK LIZARD ?")
    print("Okay then.\n")

    name = input("Please give me your name, so I don't have to call you 'Player': ")
    if name == "default" or name.strip() == "":
        print("You can't use this name!")
        sys.exit()

    if create_ifn_exist(name):
        print(f"Hello {name}, nice to meet you!")
    else:
        print(f"Hello {name}, nice to see you again!")

    stats = get_stats(name)

    mode = input("Do you want to play the easy or the hard way? [e/h]: ").lower()
    while mode != "e" and mode != "h":
        mode = input("Try again. Either use 'e' or 'h': ").lower()

    stats["mode"] = mode
    stats["game"] = [0] * 3  # lost, tie, won
    return stats


def check_won(
    player: Sign, comp: Sign, game: list
) -> int:  # 1 player won, 0 tie, -1 comp won
    result = -1
    if player == comp:
        result = 0

    if (player.value + 2) % 5 == comp.value or (player.value + 4) % 5 == comp.value:
        result = 1

    game[result + 1] += 1

    return result


def get_comp_sign(stats: dict) -> Sign:
    return Sign(random.randint(0, 4))


def get_player_sign(player_name: str, again: bool = False) -> Sign:
    sign = None

    if not again:
        ps = input(f"{player_name}, what do you choose to play? (press h for help): ")
    else:
        ps = input("Before you used an undefined character. Please try again: ")

    if ps.lower() == "h":
        print("The rules are as follows:")
        print(
            "Scissors cuts Paper covers Rock crushes Lizard poisons Spock "
            + "smashes Scissors decapitates Lizard eats Paper disproves Spock "
            + "vaporizes Rock crushes Scissors.\n"
        )

        print("For each sign you can use the following characters:")
        for x in range(5):
            y = Sign(x)
            c = y.name[0]
            if x == 2:
                c = "C"
            print(f"{y.name:8}: '{c}', '{c.lower()}', '{x}'")
        print("Press 'e' for exit")

        sign = get_player_sign(player_name)

    elif ps.lower() == "r" or ps == "0":
        sign = Sign(0)
    elif ps.lower() == "p" or ps == "1":
        sign = Sign(1)
    elif ps.lower() == "c" or ps == "2":
        sign = Sign(2)
    elif ps.lower() == "s" or ps == "3":
        sign = Sign(3)
    elif ps.lower() == "l" or ps == "4":
        sign = Sign(4)
    elif ps.lower() == "e":
        sign = None
    else:
        sign = get_player_sign(player_name, True)

    return sign


def save_result(player_name: str, player_sign: Sign, comp_sign: Sign):
    add_value(player_name, player_sign)
    add_value("default", comp_sign)


def print_won(player_name: str, won: int):
    if won == 1:
        print(f"Congratulations {player_name}, you won!")
    elif won == 0:
        print("Tie!")
    else:
        print("Too bad, you lost!")
    print()


def play(stats: dict):
    comp_sign = get_comp_sign(stats)
    player_sign = get_player_sign(stats["name"])
    if player_sign is None:
        return
    stats[player_sign.name.lower()] += 1

    won = check_won(player_sign, comp_sign, stats["game"])
    save_result(stats["name"], player_sign, comp_sign)
    print(f"Computer played: {comp_sign.name}")
    print_won(stats["name"], won)

    play(stats)


def show_stats(stats: dict):
    print(
        f"This game you won {stats['game'][2]} times, tied {stats['game'][1]} "
        + f"times and lost {stats['game'][0]} times. \n"
    )

    if (
        sum(
            [
                stats["rock"],
                stats["paper"],
                stats["scissors"],
                stats["spock"],
                stats["lizard"],
            ]
        )
        == 0
    ):
        print("You haven't used any signs so far.")
    else:
        print("Your used signs in total:")
        data = np.array(
            [
                stats["rock"],
                stats["paper"],
                stats["scissors"],
                stats["spock"],
                stats["lizard"],
            ]
        )
        labels = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
        plt.pie(data, labels=labels)
        plt.show()


def delete(player_name: str) -> bool:
    if use_DSGVO(player_name):
        print(f"User {player_name} wurde erfolgreich gelöscht!")
        return True
    print(f"User {player_name} konnte nicht gelöscht werden")
    return False


def menue(stats: dict):
    print(f"\n{stats['name']}, you are now in the menue. What do you want to do?")
    action = input(
        "Press 'p' for play, 's' for stats, 'd' for delete and 'e' for exit: "
    )

    if action[0].lower() == "p":
        play(stats)
    elif action[0].lower() == "s":
        show_stats(stats)
    elif action[0].lower() == "d":
        if delete(stats["name"]):
            return
    elif action[0].lower() == "e":
        return

    menue(stats)


def _main():
    stats = get_name_mode()
    menue(stats)

    print("Goodbye!")


if __name__ == "__main__":
    _main()
