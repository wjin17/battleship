from abc import ABC
from HitStatus import HitStatus
from enum import Enum

# {Destroyer:1, Submarine:3, Cruiser:3, Battleship:4, Carrier: 5}

class Ship(ABC):
    def __init__(self, health, name, symbol):
        self.health = health
        self.name = name
        self.symbol = symbol

    def take_hit(self):
        self.health -= 1
        if self.health == 0:
            return HitStatus.SINK
        else:
            return HitStatus.HIT

class Destroyer(Ship):
    def __init__(self):
        super().__init__(1, "Destroyer", "D")

class Submarine(Ship):
    def __init__(self):
        super().__init__(3, "Submarine", "S")

class MotorBoat(Ship):
    def __init__(self):
        super().__init__(3, "Motor boat", "M")

class Battleship(Ship):
    def __init__(self):
        super().__init__(4, "Battleship", "B")

class Carrier(Ship):
    def __init__(self):
        super().__init__(5, "Carrier", "C")

class Orientation(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def create_ships(num):
    return [Destroyer(), Submarine(), MotorBoat(), Battleship(), Carrier()][:num]

def get_orientations():
    return [Orientation.UP, Orientation.DOWN, Orientation.LEFT, Orientation.RIGHT]