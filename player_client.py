import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

def player_input_loop():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            command = input("Enter command (move x y z / status / quit): ").strip()
            if command == "quit":
                break
            s.sendall(command.encode())
            data = s.recv(1024).decode()
            print(data)

if __name__ == "__main__":
    player_input_loop()