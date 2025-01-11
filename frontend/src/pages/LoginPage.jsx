import React, { useState } from 'react';
import { MDBContainer, MDBRow, MDBCol, MDBCard, MDBCardBody, MDBInput, MDBBtn } from 'mdb-react-ui-kit';

export default function LoginPage() {
    const [loginData, setLoginData] = useState({ email: '', password: '' });

    // Mock user data as an array of users
    const mockUsers = [
        { email: "user@example.com", password: "password123" },
        { email: "admin@example.com", password: "adminpassword" },
        { email: "guest@example.com", password: "guest123" }
    ];

    const handleChange = (e) => {
        setLoginData({ ...loginData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Check if any user matches the login credentials
        const user = mockUsers.find(user => user.email === loginData.email && user.password === loginData.password);
        
        if (user) {
            console.log('Login successful!');
            alert('Login successful!');
            // Redirect or further processing
        } else {
            console.log('Login failed!');
            alert('Invalid credentials!');
        }
    };

    return (
        <MDBContainer fluid className="p-3 my-5 h-100">
            <MDBRow className="justify-content-center align-items-center h-100">
                <MDBCol col="12" md="6" lg="4">
                    <MDBCard>
                        <MDBCardBody>
                            <form onSubmit={handleSubmit}>
                                <p className="h4 text-center mb-4">Sign in</p>
                                <MDBInput className='mb-4' type='email' name='email' id='form1' label='Email' onChange={handleChange} />
                                <MDBInput className='mb-4' type='password' name='password' id='form2' label='Password' onChange={handleChange} />
                                <div className="text-center mt-4">
                                    <MDBBtn className="mb-4" type="submit">Login</MDBBtn>
                                </div>
                            </form>
                        </MDBCardBody>
                    </MDBCard>
                </MDBCol>
            </MDBRow>
        </MDBContainer>
    );
}
