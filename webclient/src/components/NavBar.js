import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';

function NavigationBar() {
return (
    <Navbar bg="dark" variant="dark" expand="lg" >
        <Container>
            <Navbar.Brand href="#home" style={{ fontSize: '30px' }}>BearRoutes</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                    <Nav.Link href="#home">Home</Nav.Link>
                    <Nav.Link href="#link">Link</Nav.Link>
                    {/* Add more Nav.Link or NavDropdown components as needed */}
                </Nav>
            </Navbar.Collapse>
        </Container>
    </Navbar>
);
}

export default NavigationBar;
