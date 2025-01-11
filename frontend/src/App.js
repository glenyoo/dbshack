// src/App.js
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Remove if not using React Router
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

// src/App.js
import React from 'react';
import AppNavbar from './components/Navbar';
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

function App() {
  return (
    <div>
      <AppNavbar />
      {/* Other components */}
    </div>
  );
}

export default App;
