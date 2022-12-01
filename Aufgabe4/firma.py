#%%
from enum import Enum
from typing import List


class Gender(Enum):
    Male = 0
    Female = 1


class Position(Enum):
    Mitarbeiter = 0
    Abteilungsleiter = 1


class Abteilung(Enum):
    Production = 0
    Sales = 1
    Aquisition = 2
    It = 3
    Accounting = 4
    HumanResources = 5
    Management = 6


def get_anz_abteilungen() -> int:
    return len(Abteilung)


class Person:

    name: str
    abteilung: Abteilung
    gender: Gender
    position: Position

    def __init__(
        self, name: str, abteilung: Abteilung, gender: Gender, position: Position
    ):
        self.name = name
        self.abteilung = abteilung
        self.gender = gender
        self.position = position


class Firma:

    name: str
    employees: List[Person]

    def __init__(self, name: str, employees: List[Person] = []):
        self.name = name
        self.employees = employees

    def get_anz_position(self, position: Position) -> int:
        return len([1 for e in self.employees if e.position == position])

    def get_biggest_branch(self) -> int:
        biggest = ("", -1)
        for b in Abteilung:
            anz = len([1 for e in self.employees if e.abteilung == b])
            if anz > biggest[1]:
                biggest = (b.name, anz)

        return biggest[0]

    def get_percent(self, gender: Gender) -> float:
        anz = len([1 for e in self.employees if e.gender == gender])
        return anz / len(self.employees)


def create_data():
    liste = []
    liste.append(Person("Franz", Abteilung.It, Gender.Male, Position.Abteilungsleiter))
    liste.append(
        Person("Monika", Abteilung.Management, Gender.Female, Position.Mitarbeiter)
    )
    liste.append(Person("Otto", Abteilung.It, Gender.Male, Position.Mitarbeiter))

    return liste


def _main():
    f = Firma("Hello world!")
    f.employees = create_data()

    print(f"Es gibt {f.get_anz_position(Position.Mitarbeiter)} Mitarbeiter")
    print(f"Es gibt {f.get_anz_position(Position.Abteilungsleiter)} Abteilungsleiter")

    print(f"Es gibt {get_anz_abteilungen()} Abteilungen")

    print(f"Die größte Mitarbeiterstärke ist die Abteilung '{f.get_biggest_branch()}'")

    print(f"{f.get_percent(Gender.Male):04.2f}% der Mitarbeiter sind männlich.")
    print(f"{f.get_percent(Gender.Female):04.2f}% der Mitarbeiter sind weiblich.")


if __name__ == "__main__":
    _main()
