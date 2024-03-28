import logo from './logo.svg';
import './App.css';
import Dot from './components/Dot';

function App() {
  return (
<div className="App">
      <div className="floor-map-container">
        <Dot x={100} y={150} color="red" />
      </div>
    </div>
    
  );
}

export default App;
