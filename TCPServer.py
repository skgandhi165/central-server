from fastapi import FastAPI
import asyncio

app = FastAPI()

async def tcp_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message} from {addr}")

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Closing the connection")
    writer.close()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(tcp_server())