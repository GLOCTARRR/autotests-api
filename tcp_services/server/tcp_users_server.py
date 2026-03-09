import socket

from tcp_services.constants import WS_SERVER_HOST, WS_SERVER_PORT


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (WS_SERVER_HOST, WS_SERVER_PORT)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен.")
    messages = list()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        messages.append(data)

        client_socket.send("\n".join(messages).encode())


if __name__ == "__main__":
    server()
