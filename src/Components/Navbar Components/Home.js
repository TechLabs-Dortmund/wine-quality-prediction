import React from 'react';
import "./Home.css";
import Button from 'react-bootstrap/Button';



const Home = () => {
  return <div>
      <img src={'/Wineglass.jpg'} alt="Wineglass" class="responsive"/>
      <h1>Vino Chance</h1>
      <h2>Dein perfekter Wein </h2>
      <div class= "justify-content-md-center">
      <Button variant="danger" size="sm" class="btn btn-primary btn-xl">Finden den Wein zu deinem Essen</Button>{' '}</div>
  </div>;



}

export default Home;
