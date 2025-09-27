import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        count = 5
        response_lines = [f"{i+1} Сообщение пользователя: {message}" for i in range(count)]
        response = "\n".join(response_lines)

        await websocket.send(response)



async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
