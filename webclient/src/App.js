import React, { useState, useEffect } from 'react';
import './App.css';
import Container from './components/MapContainer';
import NavigationBar from './components/NavBar';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [zoomLevel, setZoomLevel] = useState(1);
  const [dots, setDots] = useState([]);

  // Function to add a new dot
  const addDot = (x, y, color = 'red') => {
    const newDot = { x, y, color };
    setDots(currentDots => [...currentDots, newDot]);
  };

  useEffect(() => {
    // Replace 'ws://example.com/ws' with your WebSocket server URL
    const ws = new WebSocket('ws://localhost:8000/ws');

    ws.onopen = () => {
      console.log('WebSocket Connected');
    };

    ws.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        // Assuming the message format is { x: number, y: number, color: string }
        addDot(message.x, message.y, message.color);
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
      }
    };

    ws.onclose = () => {
      console.log('WebSocket Disconnected');
    };

    // Clean up the WebSocket connection when the component unmounts
    return () => {
      ws.close();
    };
  }, []); // Empty dependency array ensures this runs only once on mount

  return (
    <div className="App">
        <NavigationBar />
      <Container 
        zoomLevel={zoomLevel} 
        setZoomLevel={setZoomLevel}
        dots={dots} // Pass the dots as props
      />
    </div>
  );
}

export default App;
