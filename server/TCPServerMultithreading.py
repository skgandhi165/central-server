from fastapi import FastAPI
import asyncio
import asyncpg
from datetime import datetime
import threading

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

async def handle_client_1(reader, writer):
    await handle_client(reader, writer, 'bleber_1_data')

async def handle_client_2(reader, writer):
    await handle_client(reader, writer, 'bleber_2_data')

async def handle_client_3(reader, writer):
    await handle_client(reader, writer, 'bleber_3_data')

async def handle_client(reader, writer, table_name):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    while True:
        data = await reader.readline()
        if not data:
            break
        
        message = data.decode().strip()
        print(f"Received {message} from {addr}")

        message_array = message.split()
        bleber_id = message_array[2] # Not needed anymore if correct bleber is populating correct port
        device_id = message_array[9]
        radius = message_array[11][:-1]
        now = str(datetime.now())
        
        # Insert data into PostgreSQL database
        print(message)
        # async with pool.acquire() as connection:
        #     await connection.execute(f"INSERT INTO {table_name} (device_id, radius, time) VALUES ($1, $2, $3)", device_id, radius, now)
        
        # Echo back to the client
        writer.write(data)
        await writer.drain()

    print("Closing the connection")
    writer.close()

@app.on_event("startup")
async def startup_event():
    await connect_to_db()
    await clear_database()

    # Start separate threads for each socket

    # Used for nrfdevID: 0
    threading.Thread(target=start_tcp_server, args=(handle_client_1, '0.0.0.0', 50001)).start()

    # Used for nrfdevID: 1
    threading.Thread(target=start_tcp_server, args=(handle_client_2, '0.0.0.0', 50002)).start()

    # Used for nfrfdevID: 2
    threading.Thread(target=start_tcp_server, args=(handle_client_3, '0.0.0.0', 50003)).start()

def start_tcp_server(handle_client_func, host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = loop.run_until_complete(asyncio.start_server(handle_client_func, host, port))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()