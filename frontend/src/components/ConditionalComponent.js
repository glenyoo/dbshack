import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import AppNavbar from './components/Navbar';
import LoginPage from './pages/LoginPage';
import LandingPage from './pages/LandingPage';
import RequestPage from './pages/RequestPage';
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

function ConditonalComponent ({ isLoggedIn }){
    const navigate = useNavigate();

    if(isLoggedIn) {
        return (
            <div>
                <Router>
                    <div>
                    <AppNavbar />
                    <Routes>
                        <Route path="/login" element={<LoginPage />} />
                        <Route path="/home" element={<LandingPage />} />
                        <Route path="/requests" element={<RequestPage />} />
                    </Routes>
                    </div>
                </Router>
            </div>
        )
    } else {
        navigate("/login");
    }

}

export default ConditonalComponent;