import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AppNavbar from './components/Navbar';
import LoginPage from './pages/LoginPage';
import LandingPage from './pages/LandingPage';
import RequestPage from './pages/RequestPage';
import EditPage from './pages/EditPage';
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

function App() {
  return (
    <Router>
      <div>
        <AppNavbar />
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/home" element={<LandingPage />} />
          <Route path="/edit/:id" element={<EditPage />} />
          <Route path="/requests" element={<RequestPage />} />
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
