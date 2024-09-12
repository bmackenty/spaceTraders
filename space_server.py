import socket
import threading
import time
import ship_templates as st
import space_system as ss

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

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

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        command = data.strip().split()
        if command[0] == "move" and len(command) == 4:
            x, y, z = map(int, command[1:])
            ship.x = x
            ship.y = y
            ship.z = z
            response = f"Moved ship '{ship.name}' to position: x={x}, y={y}, z={z}"
        elif command[0] == "status":
            response = f"Ship '{ship.name}' status: x={ship.x}, y={ship.y}, z={ship.z}, crew={ship.crew}"
        else:
            response = "Invalid command"
        conn.sendall(response.encode())
    conn.close()

def tick_loop(cycleTime):
    cycleCount = 0
    while True:
        cycleCount += 1
        time.sleep(cycleTime)
        currentSpace.update()
        print("tick")
        currentSpace.show_objects()
        print(f"cycleCount: {cycleCount}")

# Start the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server started at {HOST}:{PORT}")

# Start the tick loop in a separate thread
tick_thread = threading.Thread(target=tick_loop, args=(3,))
tick_thread.start()

# Accept client connections
while True:
    conn, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()