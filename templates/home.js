import React from 'react';
import "./Home.css";
import Button from 'react-bootstrap/Button';
import { Container, Row, Col} from 'react-bootstrap';
import { Link } from 'react-router-dom';




const Home = () => {

  return<div className="bg">
<br></br>
<br></br>
<br></br>
<br></br><br></br>
<br></br>
<br></br>
<br></br>
  <Container>
      <h1>Find the wine.</h1>
      <h2>No matter what you eat tonight. </h2>
      <div class= "d-flex  justify-content-center">
      <Link to="/wine-finder">
      <Button size="sm" class="btn btn-primary btn-primary:hover btn-xl">Search now</Button>{' '}
      </Link>
      </div>
  </Container>

  </div>;




}

export default Home;