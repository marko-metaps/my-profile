# ws_server.py

import asyncio
import websockets
import time

async def handler(websocket, path):
    print("Client connected")
    while True:
        message = f'divId set.outerHTML <div id="divId">Message received at {time.strftime("%H:%M:%S")}</div>'
        print("Sending message:", message)
        await websocket.send(message)
        await asyncio.sleep(1)


start_server = websockets.serve(handler, "localhost", 5678)

if __name__ == "__main__":
    print(f"WebSocket server started on ws://localhost:5678")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
