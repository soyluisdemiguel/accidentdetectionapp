import asyncio
import websockets
from datetime import datetime

connected_users = set()

async def user_handler(websocket, path):
    connected_users.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            if message:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                formatted_message = f"[{timestamp}] {message}"
                await broadcast_message(formatted_message)
    except websockets.ConnectionClosed:
        pass
    finally:
        connected_users.remove(websocket)

async def broadcast_message(message):
    for user in connected_users:
        try:
            await user.send(message)
        except websockets.ConnectionClosed:
            pass

if __name__ == "__main__":
    server = websockets.serve(user_handler, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
