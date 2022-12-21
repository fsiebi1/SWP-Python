#%%

from flask import jsonify
from sqlalchemy import Column, Integer, Text, Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from dataclasses import dataclass
import json

import matplotlib.pyplot as plt
import numpy as np
from tools import Sign

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine("sqlite:///./game.sqlite3")
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
Base.query = db_session.query_property()


@dataclass
class StatsDB(Base):
    __tablename__ = "Game"  # Abbildung auf diese Tabelle

    name: str
    rock: int
    paper: int
    scissors: int
    spock: int
    lizard: int

    name = Column(Text, primary_key=True)
    rock = Column(Integer)
    paper = Column(Integer)
    scissors = Column(Integer)
    spock = Column(Integer)
    lizard = Column(Integer)

    def serialize(self):
        return {
            "name": self.name,
            "rock": self.rock,
            "paper": self.paper,
            "scissors": self.scissors,
            "spock": self.spock,
            "lizard": self.lizard,
        }


def init_db():
    Base.metadata.create_all(bind=engine)


def get_stats(name: str) -> json:
    stat = StatsDB.query.get(name)
    if stat is not None:
        return stat.serialize()
    return None


def create_ifn_exist(name: str) -> bool:  # true when created
    stat = StatsDB.query.get(name)
    if stat is None:
        db_session.add(
            StatsDB(name=name, rock=0, paper=0, scissors=0, spock=0, lizard=0)
        )
        db_session.flush()
        return True
    return False


def add_value(name: str, sign: Sign) -> bool:
    info: StatsDB
    info = StatsDB.query.get(name)
    if info is None:
        return False
    if sign == Sign(0):
        info.rock += 1
    elif sign == Sign(1):
        info.paper += 1
    elif sign == Sign(2):
        info.scissors += 1
    elif sign == Sign(3):
        info.spock += 1
    elif sign == Sign(4):
        info.lizard += 1

    db_session.add(info)
    db_session.flush()
    return True


def use_DSGVO(name: str) -> bool:
    info: StatsDB
    info = StatsDB.query.get(name)

    if info is not None:
        db_session.delete(info)
        db_session.flush()
        return True
    return False


def create_chart(stat: json, path=""):
    data = np.array(
        [stat["rock"], stat["paper"], stat["scissors"], stat["spock"], stat["lizard"]]
    )
    labels = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
    plt.pie(data, labels=labels)

    if path == "":
        plt.show()
    else:
        plt.savefig(path)


def _main():
    init_db()
    create_ifn_exist("default")
    # add_value("Hello", Sign(0))

    # stats = get_stats("Hello")
    # print(json.dumps(stats, indent=4))

    # create_chart(get_stats("Hello"))


if __name__ == "__main__":
    _main()
