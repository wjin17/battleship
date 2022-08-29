from abc import ABC, abstractmethod
from ast import literal_eval
from HitStatus import HitStatus
import os

from Player import Human, AI
from TextColor import TextColor

class Battleship(ABC):
    win = False
    @abstractmethod
    def start(self):
        pass

    # @abstractmethod
    # def __set_players(self):
    #     pass

class BattleshipAI(Battleship):
    def __init__(self, ships):
        self.player1 = Human(ships)
        self.player2 = AI(ships)
    
    def __set_players(self):
        self.player1.place_ships()
        self.player2.place_ships()
    
    def start(self):
        self.__set_players()
        winner = False
        while not winner:
            position = False
            os.system("clear")
            print("########## RADAR ##########")
            self.player1.radar.show()
            print("########## OCEAN ##########")
            self.player1.ocean.show()
            while not position:
                try:
                    position_input = literal_eval(input(TextColor.green(f"Make a guess (x, y)\n")))
                    if type(position_input) is not tuple or len(position_input) != 2: raise LookupError
                    if not self.player1.radar.check_valid_position(position_input): raise LookupError
                    position = position_input
                    print(position)
                except ValueError:
                    print(TextColor.yellow("Invalid position, must be in the form of (x, y)"))
                except LookupError:
                    print(TextColor.red("Invalid position, try again"))
            
            # record hit
            p2_status, message = self.player2.take_hit(position)
            
            if p2_status == HitStatus.MISS: 
                print(TextColor.yellow(message))
            elif p2_status == HitStatus.HIT: 
                print(TextColor.green(message))
            elif p2_status == HitStatus.WIN:
                print("You won!")
                winner = "Player1"
                break
            self.player1.record_guess(position, p2_status)

            ai_guess = self.player2.make_guess()
            p1_status, message = self.player1.take_hit(ai_guess)
            print(message)

            if p1_status == HitStatus.WIN:
                print("You won!")
                winner = "Player2"
                break
            
            self.player2.record_guess(ai_guess, p1_status)


class BattleshipPVP(Battleship):
    pass