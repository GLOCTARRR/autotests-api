import socket
import sys

from tcp_services.constants import WS_SERVER_HOST, WS_SERVER_PORT


def send_and_recv_message(message: str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (WS_SERVER_HOST, WS_SERVER_PORT)
    client_socket.connect(server_address)

    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Ответ от сервера:\n")
    print(response)

    client_socket.close()


if __name__ == "__main__":
    message = sys.argv[1]
    send_and_recv_message(message)
