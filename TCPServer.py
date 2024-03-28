from fastapi import FastAPI
import asyncio
import asyncpg
from datetime import datetime

app = FastAPI()

# Database connection pool
pool = None

async def clear_database():
    async with pool.acquire() as connection:
        await connection.execute("DELETE FROM device_data")

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
    server = await asyncio.start_server(handle_client, '0.0.0.0', 50001)

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

        message_array = message.split()
        bleber_id = message_array[2]
        device_id = message_array[9]
        radius = message_array[12][:-1]
        now = str(datetime.now())
        
        # Insert data into PostgreSQL database
        async with pool.acquire() as connection:
            # await connection.execute("INSERT INTO device_data (device_id, radius, time) VALUES ($1, $2, $3)", *message.split(), now)
            if bleber_id == '0,':
                await connection.execute("INSERT INTO bleber_1_data (device_id, radius, time) VALUES ($1, $2, $3)", device_id, radius, now)
            elif bleber_id == '1,':
                await connection.execute("INSERT INTO bleber_2_data (device_id, radius, time) VALUES ($1, $2, $3)", device_id, radius, now)
            elif bleber_id == '2,':
                await connection.execute("INSERT INTO bleber_3_data (device_id, radius, time) VALUES ($1, $2, $3)", device_id, radius, now)
        # Echo back to the client
        writer.write(data)
        await writer.drain()

    print("Closing the connection")
    writer.close()

@app.on_event("startup")
async def startup_event():
    await connect_to_db()
    await clear_database()
    asyncio.create_task(tcp_server())
