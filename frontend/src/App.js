import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Requests from './pages/Requests';
import SignOut from './pages/SignOut';
import AppNavbar from './components/Navbar';
import RequestContainer from './components/RequestContainer';
import RequestForm from './components/RequestForm';
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

function App() {
  return (
    <Router>
      <div>
        <AppNavbar />
        <Routes>
          <Route path="/pages/" element={<Home />} />
          <Route path="/pages/requests" element={<Requests />} />
          <Route path="/pages/signout" element={<SignOut />} />
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
