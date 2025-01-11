import React from 'react';
import { MDBNavbar, MDBContainer, MDBNavbarBrand, MDBNavbarNav, MDBNavbarItem, MDBNavbarLink } from 'mdb-react-ui-kit';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <MDBNavbar expand='lg' light bgColor='light'>
      <MDBContainer fluid>
        <MDBNavbarBrand>
          <Link to="/pages/" className="navbar-brand">BrandName</Link>
        </MDBNavbarBrand>
        <MDBNavbarNav right fullWidth={false} className='mb-2 mb-lg-0'>
          <MDBNavbarItem>
            <Link to="/pages/" className="navbar-brand">Home</Link>
          </MDBNavbarItem>
          <MDBNavbarItem>
            <Link to="/pages/requests" className="navbar-brand">Requests</Link>
          </MDBNavbarItem>
          <MDBNavbarItem>
            <Link to="/pages/signout" className="navbar-brand">Signout</Link>
          </MDBNavbarItem>
        </MDBNavbarNav>
      </MDBContainer>
    </MDBNavbar>
  );
}
