import socket

# Server address and port
server_address = ('127.0.0.1', 8888)

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect(server_address)
    
    while True:
        # Get input message from user
        message = input("Enter message to send (type 'quit' to exit): ")
        
        # Send message to the server
        s.sendall(message.encode())
        
        # If user wants to quit, break the loop
        if message.lower() == 'quit':
            break
        
        # Receive response from the server
        data = s.recv(1024)
        
        # Print the received message from the server
        print('Received:', data.decode())