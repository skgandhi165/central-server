import React from 'react';

const Dot = ({ x, y, zoom, color }) => {
  const size = 5; // Default size of the dot, adjust based on zoom if necessary

  const dotStyle = {
    position: 'absolute',
    width: `${size}px`,
    height: `${size}px`,
    backgroundColor: color,
    borderRadius: '50%',
    left: `${x - size / 2}px`, // Center the dot on x, y
    top: `${y - size / 2}px`, // Adjust these calculations as needed
    transform: 'translate(-50%, -50%)',
  };

  return <div style={dotStyle}></div>;
};

export default Dot;
