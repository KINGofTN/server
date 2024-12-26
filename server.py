import socket
import os


# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
#PORT = 5000       # Port to listen on
PORT = int(os.getenv('PORT', 5000))
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server started on {HOST}:{PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    conn.sendall(data)  # Echo back the data

if __name__ == "__main__":
    start_server()
