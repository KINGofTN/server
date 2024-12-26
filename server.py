import socket
import threading

clients = []  # List to keep track of all connected clients

def broadcast(message, sender_socket):
    """
    Send a message to all clients except the sender.
    """
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # Remove the client if sending fails
                clients.remove(client)

def handle_client(client_socket, address):
    """
    Handle incoming messages from a client and broadcast them to others.
    """
    print(f"[NEW CONNECTION] {address} connected.")
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
    except ConnectionResetError:
        print(f"[DISCONNECT] {address} disconnected.")
    finally:
        clients.remove(client_socket)
        client_socket.close()

def start_server(host='0.0.0.0', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {len(clients)}")

if __name__ == "__main__":
    start_server()
