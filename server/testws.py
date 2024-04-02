from fastapi import FastAPI, WebSocket
import json
from random import randint
from time import sleep

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for _ in range(100):
        # Generate a random point
        x = randint(0, 10)  # Assuming 1791 is the map width in pixels
        y = randint(0, 10)  # Assuming 1484 is the map height in pixels
        color = "blue"  # Static color for simplicity, can be randomized as well
        message = json.dumps({"x": x, "y": y, "color": color})
        
        # Send the message through the WebSocket
        await websocket.send_text(message)
         # Wait for a bit before sending the next message
        sleep(1)  # Adjust the sleep duration as needed (in seconds)
    
    await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
