import socket
import threading
import os

# List to keep track of connected clients and their IDs
clients = []
client_ids = {}

# Broadcast function to send messages to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:  # Don't send the message back to the sender
            try:
                client.send(message)
            except:
                clients.remove(client)
                del client_ids[client]

# Function to handle communication with a single client
def handle_client(client_socket, client_address):
    # Assign a unique ID to each client
    client_id = f"Client {len(clients) + 1}"
    client_ids[client_socket] = client_id
    clients.append(client_socket)

    print(f"{client_id} connected from {client_address}")
    client_socket.send(f"Welcome, {client_id}!".encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            full_message = f"{client_ids[client_socket]}: {message}"
            print(full_message)
            broadcast(full_message.encode('utf-8'), client_socket)
        except:
            print(f"{client_ids[client_socket]} disconnected")
            clients.remove(client_socket)
            del client_ids[client_socket]
            break

    client_socket.close()

def main():
    host = '0.0.0.0'  # Bind to all interfaces
    port = int(os.environ.get('PORT', 5000))  # Use Railway-assigned port or fallback
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server is running on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    main()
