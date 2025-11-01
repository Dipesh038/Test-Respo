import socket

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server details
SERVER_IP = '10.30.60.79'
SERVER_PORT = 9999

# Your name
name = "Dipesh"

print("UDP Client is running... Type your message below.")

while True:
    # Take message from user
    message = input(f"{name}: ")

    # Combine name and message
    full_message = f"{name}: {message}"

    # Send message to server
    client.sendto(full_message.encode(), (SERVER_IP, SERVER_PORT))

    # Exit condition
    if message.lower() == 'bye':
        print("Connection closed.")
        break

    # Receive response from server
    data, addr = client.recvfrom(1024)
    print("Server:", data.decode())

# Close socket
client.close()
