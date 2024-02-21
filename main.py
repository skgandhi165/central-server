from fastapi import FastAPI, WebSocket

app = FastAPI()

# List to store connected websocket clients
connected_clients = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  connected_clients.append(websocket)

  try:
    while True:
      # Wait for data from the client
      data = await websocket.receive_text()
      print(f"Received message: {data}")

      # Echo the received message back to the client
      await websocket.send_text(f"Message text was: {data}")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    # Remove the client when the connection is closed
    connected_clients.remove(websocket)


# Function to send a message to all connected clients
async def send_to_all(message: str):
  for client in connected_clients:
    await client.send_text(message)


# Example of sending a message to all connected clients from another endpoint
@app.post("/send_message")
async def send_message_to_all_clients(message: str):
  await send_to_all(message)
  return {"message": "Message sent to all clients"}
