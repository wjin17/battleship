from Battleship import BattleshipAI

def game_loop(mode):
    if True: #mode.lower() == "ai":
        print("doing ai")
        battleship = BattleshipAI(2)
        battleship.start()
        pass
    else:
        print("doing pvp")
        pass

if __name__ == "__main__":
    modes = ["pvp", "ai"]
    mode = input("Which gamemode? PVP or AI\n").lower()
    while mode not in modes:
        mode = input("Enter a valid gamemode\n").lower()

    game_loop(mode)