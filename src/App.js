import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import { Container, Nav, Navbar, NavbarBrand } from 'react-bootstrap';
import {
  BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import Information from './Components/Navbar Components/Information';
import Wine from './Components/Navbar Components/Wine';
import Food from './Components/Navbar Components/Food';
import Goodcheap from './Components/Navbar Components/Goodcheap';
import Home from './Components/Navbar Components/Home';
import Footer from './Components/Footer/Footer';



function App() {
  return (
    <div className="App">
      <Router>
      <Navbar
      bg="myRed" variant="dark">
        <NavbarBrand>
          Vino Chance 
        </NavbarBrand>

      
      <Nav className="me-auto">
        <Nav.Link as={Link}to={"/Home"}>Home</Nav.Link>
        <Nav.Link as={Link}to={"/Ueber-Wein"}>Über Wein</Nav.Link>
        <Nav.Link as={Link}to={"/Wein"}>Weine entdecken</Nav.Link>
        <Nav.Link as={Link}to={"/Gericht"}>Gerichte finden</Nav.Link>
        <Nav.Link as={Link}to={"/GutundGuenstig"}>Gut und Günstig</Nav.Link>
    </Nav>
    
      </Navbar>
        <div>
        <Routes>
            <Route path="Home" element={<Home/>} />
            <Route path="Ueber-Wein" element={<Information/>} />
            <Route path="Wein" element={<Wine/>} />
            <Route path="Gericht" element={<Food/>} />
            <Route path="GutundGuenstig" element={<Goodcheap/>} />
          </Routes>
        </div>
    </Router>
  
    <Footer/>
      </div>
  


  );

  

  
}


export default App;
