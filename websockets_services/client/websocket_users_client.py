import asyncio

import websockets

from websockets_services.constants import WS_SERVER_PORT, WS_SERVER_HOST

async def client():
    uri = f"ws://{WS_SERVER_HOST}:{WS_SERVER_PORT}"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")

asyncio.run(client())
