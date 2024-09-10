import os
os.system('clear')

import space_system as ss
import ship_templates as st

# Create a new system
currentSpace = ss.SpaceSystem()

# create a ship
ship = st.ShipTemplate(name="Explorer", speed=10, crew=100)
currentSpace.add_object(ship)  # Add the ship to the system.

# print the objects in the system
currentSpace.show_objects()
