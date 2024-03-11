from fastapi import FastAPI
import asyncio
import asyncpg

app = FastAPI()

# Database connection pool
pool = None

async def connect_to_db():
    global pool
    pool = await asyncpg.create_pool(
        user='postgres',
        password='BIWiMYaXzIvwsLfmtHhrhJITehjpcCBv',
        database='railway',
        host='viaduct.proxy.rlwy.net',
        port='37675'
    )

async def tcp_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    while True:
        data = await reader.readline()
        if not data:
            break
        
        message = data.decode().strip()
        print(f"Received {message} from {addr}")
        
        # Insert data into PostgreSQL database
        async with pool.acquire() as connection:
            await connection.execute("INSERT INTO bt_data (device_id, radius) VALUES ($1, $2)", *message.split())
        
        # Echo back to the client
        writer.write(data)
        await writer.drain()

    print("Closing the connection")
    writer.close()

@app.on_event("startup")
async def startup_event():
    await connect_to_db()
    asyncio.create_task(tcp_server())
