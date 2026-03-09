import asyncio

import websockets
from websockets import ServerConnection

from websockets_services.constants import WS_SERVER_HOST, WS_SERVER_PORT


async def message_handler(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"
        for _ in range(5):
            await websocket.send(response)


async def main():
    server = await websockets.serve(message_handler, WS_SERVER_HOST, WS_SERVER_PORT)
    print(f"WebSocket сервер запущен на ws://{WS_SERVER_HOST}:{WS_SERVER_PORT}")
    await server.wait_closed()


asyncio.run(main())
