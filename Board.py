from typing import Text
from HitStatus import HitStatus
from Ships import Ship, Orientation, Submarine
from abc import ABC, abstractmethod
from TextColor import TextColor

class Board:
    water = TextColor.blue(".")
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[TextColor.blue(".") for _ in range(width)] for _ in range(height)]

    @abstractmethod
    def mark_hit(self):
        pass

    def check_valid_position(self, position):
        x, y = position
        if ((0 <= x <= 9) or (0 <= y <= 9)) and (self.board[y][x] == self.water):
            return True
        else:
            return False
    
    def show(self):
        cols = " ".join([str(i) for i in range(self.width)])
        line = "".join(["-" for _ in range(self.width * 2 - 1)])
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if col_index == 0:
                    print(f"{row_index}| {col}", end=" ")
                elif col_index == self.width - 1:
                    print(col)
                else:
                    print(col, end=" ")
        print(f"Y  {line}")
        print(f" X {cols}")

class Radar(Board):
    def __init__(self):
        super().__init__(10, 10)
    
    def mark_hit(self, position, status):
        x, y = position
        if status == HitStatus.HIT or status == HitStatus.SINK:
            self.board[y][x] = TextColor.red("X")
        else:
            self.board[y][x] = "O"

class Ocean(Board):
    def __init__(self):
        super().__init__(10, 10)
    
    def check_valid_orientation(self, position, size, orientation):
        x, y = position
        if orientation == Orientation.UP:
            if ((y - size >= -1) and 
                all([self.board[row][x] == self.water for row in range(y, y - size, -1)])
                ):
                return True
            else:
                return False
        elif orientation == Orientation.DOWN:
            if ((y + size <= 10) and
                all([self.board[row][x] == self.water for row in range(y, y + size)])):
                return True
            else:
                return False
        elif orientation == Orientation.LEFT:
            if ((x - size >= -1) and
                all([self.board[y][col] == self.water for col in range(x, x - size, -1)])):
                return True
            else:
                return False
        elif orientation == Orientation.RIGHT:
            if ((x + size <= 10) and
                all([self.board[y][col] == self.water for col in range(x, x + size)])):
                return True
            else:
                return False

    def place_ship(self, ship: Ship, position, orientation):
        x, y = position
        valid_position = self.check_valid_position(position)
        valid_orientation = self.check_valid_orientation(position, ship.health, orientation)
        if valid_position and valid_orientation:
            if orientation == Orientation.UP:
                for row_index in range(y, y - ship.health, -1):
                    self.board[row_index][x] = ship.symbol
                return True
            elif orientation == Orientation.DOWN:
                for row_index in range(y, y + ship.health):
                    self.board[row_index][x] = ship.symbol
                return True
            elif orientation == Orientation.LEFT:
                for col_index in range(x, x - ship.health, -1):
                    self.board[y][col_index] = ship.symbol
                return True
            elif orientation == Orientation.RIGHT:
                for col_index in range(x, x + ship.health):
                    self.board[y][col_index] = ship.symbol
                return True
            else:
                return False
        else:
            return False
    
    def mark_hit(self, position):
        x, y = position
        symbol = self.board[y][x]
        if symbol != self.water:
            self.board[y][x] = TextColor.red("X")
        else:
            self.board[y][x] = "O"
        return symbol


if __name__ == "__main__":
    # board = Radar()
    # board.mark_hit((5, 8), HitStatus.HIT)
    # board.print()

    ocean = Ocean()
    sub = Submarine()

    ocean.place_ship((5,7), sub, Orientation.UP)
    ocean.mark_hit((5,7))


    ocean.show()