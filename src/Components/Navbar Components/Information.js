import React from 'react';
import "./Information.css";
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';

const Information = () => {
  return <div>
    <br></br>
  <br></br>

  <CardGroup>
  <Card className="card1" mt-10>
    <Card.Body>
      <Card.Title className='cardtitle'>Wineglossary</Card.Title>
      <Card.Text className='cardtext'>
        grape varieties, wine countries and wine regions
      </Card.Text>
    </Card.Body>
  </Card>
  <Card className="card2">
    <Card.Body>
      <Card.Title className='cardtitle'>Winestyles</Card.Title>
      <Card.Text className='cardtext'>
       Riesling, Dopio, Passo...{' '}
      </Card.Text>
    </Card.Body>
  </Card>
  <Card className="card3">
    <Card.Body>
      <Card.Title className='cardtitle'>Wineschool</Card.Title>
      <Card.Text className='cardtext'>
        How to grow and harvest wine
      </Card.Text>
    </Card.Body>
  </Card>
</CardGroup>
</div>;
};

export default Information;
