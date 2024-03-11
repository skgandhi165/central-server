import socket

# Server address and port
server_address = ('127.0.0.1', 8888)

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect(server_address)
    
    # Open the file for reading
    with open("data.txt", "r") as file:
        # Read file line by line
        for line in file:
            # Strip newline character and split by space to separate device ID and radius
            device_id, radius = line.strip().split()
            
            # Construct the message to send to the server
            message = f"{device_id} {radius}\n"  # Make sure to add newline at the end
            
            # Send message to the server
            s.sendall(message.encode())
            
            # Receive response from the server
            data = s.recv(1024)
            
            # Print the received message from the server
            print('Received:', data.decode())