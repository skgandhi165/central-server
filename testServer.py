import socket

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 50001       # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind the socket to the address and port
    s.listen()  # Listen for incoming connections
    print(f"Server is listening on {HOST}:{PORT}")
    conn, addr = s.accept()  # Accept a new connection
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # Receive data from the client
            if not data:
                break  # Break the loop if no data is received
            print('Received', data.decode())  # Print the received message