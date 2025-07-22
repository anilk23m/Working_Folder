import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print(f"Connected to server at {host}:{port}")

while True:
    # Send message to server
    msg = input("Client: ")
    client_socket.sendall(msg.encode())
    if msg.lower() == 'exit':
        break

    # Receive response from server
    server_reply = client_socket.recv(1024).decode()
    if not server_reply or server_reply.lower() == 'exit':
        print("Server disconnected.")
        break
    print("Server:", server_reply)

client_socket.close()
