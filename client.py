import socket

def main():
    host = '127.0.0.1'  # Replace with server's public IP or domain when deployed
    port = 12345
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    print(f"Connected to server at {host}:{port}")
    while True:
        try:
            message = input("You: ")
            client.send(message.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(f"Server: {response}")
        except:
            print("Disconnected from the server.")
            break
    client.close()

if __name__ == "__main__":
    main()

