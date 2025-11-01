import socket
import threading
import sys

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(2048).decode()
            if not message:
                print("Disconnected from server.")
                sock.close()
                sys.exit()
            print(message)
        except:
            sock.close()
            break

# Connect to server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('10.30.60.79', 12345))

# Start receiving thread
threading.Thread(target=receive_messages, args=(server,), daemon=True).start()

# Sending messages
while True:
    message = input()
    server.send(message.encode())
    print(f"<You> {message}")
    if message.lower() == 'bye':
        server.close()
        sys.exit()