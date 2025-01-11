// src/Navbar.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom'; // Remove if not using React Router

function Navbar() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="navbar">
            <span className="navbar-logo">Logo</span>
            <div className={`nav-items ${isOpen ? "open" : ""}`}>
                <Link to="/" onClick={() => setIsOpen(false)}>Home</Link>
                <Link to="/about" onClick={() => setIsOpen(false)}>About</Link>
                <Link to="/services" onClick={() => setIsOpen(false)}>Services</Link>
                <Link to="/contact" onClick={() => setIsOpen(false)}>Contact</Link>
            </div>
            <button className="nav-toggle" onClick={() => setIsOpen(!isOpen)}>
                {isOpen ? "Close" : "Menu"}
            </button>
        </nav>
    );
}

export default Navbar;
