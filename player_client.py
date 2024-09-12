import threading
import time

class Player:
    def __init__(self, ship):
        self.ship = ship

    def move(self, x, y, z):
        self.ship.x = x
        self.ship.y = y
        self.ship.z = z
        print(f"Moved ship '{self.ship.name}' to position: x={x}, y={y}, z={z}")

    def status(self):
        print(f"Ship '{self.ship.name}' status: x={self.ship.x}, y={self.ship.y}, z={self.ship.z}, crew={self.ship.crew}")

def player_input_loop(player):
    while True:
        # Get player input
        command = input("Enter command (move x y z / status / quit): ").strip().split()
        if command[0] == "move" and len(command) == 4:
            x, y, z = map(int, command[1:])
            player.move(x, y, z)
        elif command[0] == "status":
            player.status()
        elif command[0] == "quit":
            break
        else:
            print("Invalid command")

def tick_loop(currentSpace, cycleTime):
    cycleCount = 0
    while True:
        cycleCount += 1
        time.sleep(cycleTime)
        currentSpace.update()
        print("tick")
        currentSpace.show_objects()
        print(f"cycleCount: {cycleCount}")