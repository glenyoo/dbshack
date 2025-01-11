import React from 'react';
import { MDBNavbar, MDBContainer, MDBNavbarBrand, MDBNavbarNav, MDBNavbarItem, MDBNavbarLink } from 'mdb-react-ui-kit';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <MDBNavbar expand='lg' light bgColor='light'>
      <MDBContainer fluid>
        <MDBNavbarBrand>
          <Link to="/" className="navbar-brand">BrandName</Link>
        </MDBNavbarBrand>
        <MDBNavbarNav right fullWidth={false} className='mb-2 mb-lg-0'>
          <MDBNavbarItem>
            {/* <MDBNavbarLink as={Link} to="/">Home</MDBNavbarLink> */}
            <Link to="/" className="navbar-brand">Home</Link>
          </MDBNavbarItem>
          <MDBNavbarItem>
            {/* <MDBNavbarLink as={Link} to="/about">About</MDBNavbarLink> */}
            <Link to="/about" className="navbar-brand">About</Link>

          </MDBNavbarItem>
          <MDBNavbarItem>
            {/* <MDBNavbarLink as={Link} to="/services">Services</MDBNavbarLink> */}
            <Link to="/services" className="navbar-brand">Services</Link>

          </MDBNavbarItem>
          <MDBNavbarItem>
            {/* <MDBNavbarLink as={Link} to="/contact">Contact</MDBNavbarLink> */}
            <Link to="/contact" className="navbar-brand">Contact</Link>

          </MDBNavbarItem>
        </MDBNavbarNav>
      </MDBContainer>
    </MDBNavbar>
  );
}
