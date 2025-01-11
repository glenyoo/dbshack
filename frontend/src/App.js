// src/App.js
import React from 'react';
import Navbar from './Navbar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Remove if not using React Router

function App() {
  return (
    <Router> {/* Remove <Router> and related components if not using React Router */}
      <div>
        <Navbar />
        <Routes> {/* Replace <Routes> with your components if not using React Router */}
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() { return <h1>Home Page</h1>; }
function About() { return <h1>About Page</h1>; }
function Services() { return <h1>Services Page</h1>; }
function Contact() { return <h1>Contact Page</h1>; }

export default App;
