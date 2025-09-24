import asyncio
import websockets

async def handler(websocket):
    print("Client connected!")
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
            await websocket.send(f"Server received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Error in handler: {e}")

async def main():
    try:
        async with websockets.serve(handler, "localhost", 8765):
            print("Server started on ws://localhost:8765")
            await asyncio.Future()
    except KeyboardInterrupt:
        print("Server stopped by user")
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
