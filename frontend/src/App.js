// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';
import Services from './Services';
import Contact from './Contact';
import Login from './Login';
import AppNavbar from './components/Navbar';
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

function App() {
  return (
    <Router>
      <div>
        <AppNavbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>

        
      </div>
    </Router>
  );

  // return (
  //   <div>
  //     <AppNavbar />
  //     {/* <Login /> */}
  //   </div>
  // );
}


export default App;
