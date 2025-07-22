import socket

host = '127.0.0.1'
port = 12345

# Create and configure the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    if not client_msg or client_msg.lower() == 'exit':
        print("Client disconnected.")
        break
    print("Client:", client_msg)

    # Send response to client
    server_msg = input("Server: ")
    conn.sendall(server_msg.encode())
    if server_msg.lower() == 'exit':
        break

conn.close()
server_socket.close()
