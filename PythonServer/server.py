import socket
import json
from scripts import SentimentAnalysisModel

# Configuration
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

# Load the model
model = SentimentAnalysisModel()

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Listen for connections
server_socket.listen()
print(f"Listening on port {PORT}...")

# Accept a connection
client_socket, address = server_socket.accept()
print(f"Accepted connection from {address}.")

try:
    while True:
        data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        if not data:
            break
        print(f"Received data from client: {data}")

        # Make a prediction
        result = model.predict(data)

        # Send the result back to the client
        result_json = json.dumps(result)
        client_socket.sendall(result_json.encode("utf-8"))
        print(f"Sent prediction to client: {result_json}")
except Exception as e:
    print(e)
finally:
    # Close the connection
    client_socket.close()
    server_socket.close()
    print("Connection closed.")
