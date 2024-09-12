import ship_templates as st
import space_system as ss
from player_client import Player, player_input_loop, tick_loop
import threading

# how many seconds to wait between updates
cycleTime = 3

# Create a new system
currentSpace = ss.SpaceSystem()

# create a ship
ship = st.ShipTemplate(name="Explorer", speed=1, crew=100)
currentSpace.add_object(ship)  # Add the ship to the system.

# create another ship
ship2 = st.ShipTemplate(name="Scout", speed=2, crew=10, x=50, y=50, z=50)
currentSpace.add_object(ship2)  # Add the ship to the system.

# print the objects in the system
currentSpace.show_objects()

# create a player
player = Player(ship)

# Create and start the player input thread
player_thread = threading.Thread(target=player_input_loop, args=(player,))
player_thread.start()

# Run the tick loop in the main thread
tick_loop(currentSpace, cycleTime)