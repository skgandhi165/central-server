import React, { useState } from 'react';
import './App.css';
import Container from './components/MapContainer';

function App() {
  const [zoomLevel, setZoomLevel] = useState(1);
  const [dots, setDots] = useState([]);

  // Function to add a new dot
  const addDot = (x, y, color = 'red') => {
    const newDot = { x, y, color };
    setDots(currentDots => [...currentDots, newDot]);
  };


  // Function to handle button click
  const handleAddDotClick = () => {
    // Generate random x, y within the map dimensions for demonstration
    // You might want to replace this with specific logic to determine where to add the dot
    const x = Math.floor(Math.random() * 10);
    const y = Math.floor(Math.random() * 10);
    addDot(x, y, 'blue'); // Add a new dot with random position
  };

  return (
    <div className="App">
      <button onClick={handleAddDotClick}>Add Dot</button>
      <Container 
        zoomLevel={zoomLevel} 
        setZoomLevel={setZoomLevel}
        dots={dots} // Pass the dots as props
      />
    </div>
  );
}

export default App;
