import random
from ast import literal_eval
#from inquirer import Text
from abc import ABC, abstractmethod
from typing import Text

from Board import Radar, Ocean
from HitStatus import HitStatus
from Ships import create_ships, get_orientations, Orientation
from TextColor import TextColor

class Player(ABC):
    def __init__(self, num_ships):
        self.radar = Radar()
        self.ocean = Ocean()
        self.ships = {ship.symbol:ship for ship in create_ships(num_ships)}

    @abstractmethod
    def place_ships(self):
        pass

    def take_hit(self, position):
        hit = self.ocean.mark_hit(position)
        if hit in self.ships:
            status = self.ships[hit].take_hit()
            if status == HitStatus.SINK:
                sunken_ship = self.ships[hit]
                del self.ships[hit]
                if len(self.ships) == 0:
                    return (HitStatus.WIN, f"You just sank my last ship")
                else:
                    return (status, f"You just sank my {sunken_ship.name}")
            else:
                return (status, "Hit")
        else:
            return (HitStatus.MISS, "Miss")

    def record_guess(self, position, status):
        self.radar.mark_hit(position, status)

class Human(Player):
    orientations = {
        "up": Orientation.UP,
        "down": Orientation.DOWN,
        "left": Orientation.LEFT,
        "right": Orientation.RIGHT
    }

    def __init__(self, num_ships):
        super().__init__(num_ships)

    def place_ships(self):
        for ship in self.ships.values():
            position = False
            orientation = False
            while not position or not orientation:
                self.ocean.show()
                print("Ship: ", ship.symbol * ship.health)
                try:
                    if not position:
                        position_input = literal_eval(input(TextColor.green(f"Where do you want to place your {ship.name}? (x, y)\n")))
                        if type(position_input) is not tuple or len(position_input) != 2: raise ValueError
                        if not self.ocean.check_valid_position(position_input): raise LookupError
                        position = position_input
                    
                    if ship.health == 1:
                        orientation = Orientation.UP

                    if not orientation:
                        orientation_input = input(TextColor.green(f"Which direction? (up, down, left, right)\n")).lower()
                        if orientation_input not in self.orientations: raise ValueError
                        if not self.ocean.check_valid_orientation(position, ship.health, 
                                                                  self.orientations[str(orientation_input)]): raise LookupError
                        orientation = self.orientations[str(orientation_input)]

                    if not self.ocean.place_ship(ship, position, orientation):
                        raise LookupError

                except ValueError:
                    if not position:
                        print(TextColor.yellow("Invalid position, must be in the form of (x, y)"))
                    elif not orientation:
                        print(TextColor.yellow("Invalid orientation, must be up, down, left, or right"))
                    else:
                        position = orientation = False
                        print(TextColor.red("Invalid placement, try again"))
                except LookupError:
                    if not position:
                        print(TextColor.yellow("Position taken, enter new position"))
                    elif not orientation:
                        print(TextColor.yellow("Invalid orientation, enter new orientaion"))

        
        self.ocean.show()
        

class AI(Player):
    def __init__(self, num_ships):
        super().__init__(num_ships)
    
    def _find_positions(self, position, size):
        valid_position = self.ocean.check_valid_position(position)
        if valid_position:
            return [orientation for orientation in get_orientations() if self.ocean.check_valid_orientation(position, size, orientation)]
        else:
            return []
    
    def place_ships(self):
        for ship in self.ships.values():
            position = (random.randrange(10), random.randrange(10))
            available_positions = self._find_positions(position, ship.health)
            while not available_positions:
                position = (random.randrange(10), random.randrange(10))
                available_positions = self._find_positions(position, ship.health)
            
            self.ocean.place_ship(ship, position, random.choice(available_positions))
    
    def make_guess(self):
        position = (random.randrange(10), random.randrange(10))
        while (self.radar.board[position[1]][position[0]] == TextColor.red("X") or
                self.radar.board[position[1]][position[0]] == "O"):
            position = (random.randrange(10), random.randrange(10))
        return position

if __name__ == "__main__":
    # player = Human(2)
    # player.place_ships()
    # guess1 = (2,1)
    # guess2 = (1,1)
    # player.take_hit(guess1)
    # player.take_hit(guess2)
    # print("OCEAN:")
    # player.ocean.show()

    # player.record_guess(guess2, HitStatus.MISS)
    # player.record_guess(guess1, HitStatus.HIT)
    # print("RADAR:")
    # player.radar.show()
    player = AI(5)
    player.place_ships()
    print("######### OCEAN #########")
    player.ocean.show()

    # for _ in range(50):
    #     guess1 = player.make_guess()
    #     player.record_guess(guess1, random.choice([HitStatus.HIT, HitStatus.MISS, HitStatus.SINK]))

    # print("######### RADAR #########")
    # player.radar.show()
    pass