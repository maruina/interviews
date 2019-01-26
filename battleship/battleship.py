import sys

X = 10
Y = 10
SHIPS = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}


def validate_coordinates(x, y):
    if 0 <= int(x) < X and 0 <= int(y) < Y:
        return True
    else:
        return False


def exit():
    print(f"The only winning move is not to play.")
    sys.exit(0)


if __name__ == "__main__":
    user_input = input(f"Greeting Professor Falken. Shall we play a game? [y/n]: ")
    if user_input.lower() != "y":
        exit()
    while True:
        try:
            user_input = input("Insert coordinates (x,y): ")
            ux, uy = user_input.split(",")
            if not validate_coordinates(ux, uy):
                print(f"Invalid coordinates. The grid is {X} * {Y}")
        except KeyboardInterrupt:
            exit()
