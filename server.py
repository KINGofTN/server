import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{client_address}: {message}")
            client_socket.send(f"Echo: {message}".encode('utf-8'))
        except:
            print(f"Connection with {client_address} lost.")
            break
    client_socket.close()

def main():
    host = '0.0.0.0'  # To allow connections from any IP
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()

