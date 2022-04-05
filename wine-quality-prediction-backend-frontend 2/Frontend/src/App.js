import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import { Container, Nav, Navbar, NavbarBrand } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import { Button,  FormControl } from "react-bootstrap";
import {
  BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import Information from './Components/Navbar Components/Information';
import Wine from './Components/Navbar Components/Wine';
import Home from './Components/Navbar Components/Home';
import Footer from './Components/Footer/Footer';
import logo from './img/Vinochance.png';



function App() {
  return (
    <div className="App">

      <Router>
      <Navbar
      bg="myRed" variant="dark">
        <NavbarBrand>
          <img
          src={logo}
          width="30"
          height="30"
          alt="logo"/>
        </NavbarBrand>

      
      <Nav className="me-auto">
        <Nav.Link as={Link}to={"/home"}>home</Nav.Link>
        <Nav.Link as={Link}to={"/about-wine"}>about wine</Nav.Link>
        <Nav.Link as={Link}to={"/wine-finder"}>wine finder</Nav.Link>
    </Nav>
    

    <Form className="d-flex">
        <FormControl
          type="search"
          placeholder="search"
          className="me-2"
          aria-label="search"
        />
        <Button variant="outline-secondary">search</Button>
      </Form>

      </Navbar>
        <div>
        <Routes>
            <Route path="home" element={<Home/>} />
            <Route path="about-wine" element={<Information/>} />
            <Route path="wine-finder" element={<Wine/>} />

          </Routes>
        </div>
    </Router>

      

  
    <Footer/>
      </div>
  


  );

  

  
}


export default App;
