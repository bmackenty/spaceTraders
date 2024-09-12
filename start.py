import os
os.system('clear')

import space_system as ss
import ship_templates as st
import time

# how many seconds to wait between updates
cycleTime = 3
cycleCount = 0

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

#create a "tick" function to update the system
def tick(cycleTime, cycleCount):
   
    time.sleep(cycleTime)
    currentSpace.update()
    print("tick")
    currentSpace.show_objects()

# run the tick function
while True:
    cycleCount += 1
    tick(cycleTime, cycleCount) # Update the system.
    print(f"cycleCount: {cycleCount}")
