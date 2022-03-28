import React from 'react'

const CharacterItem = ({item}) => {
    return ( 
    <div className='cardSearch'>
    <div className='cardSearch-inner'>
      <div className='cardSearch-front'>
        <img src={item.img} alt='' />
      </div>
      <div className='cardSearch-back'>
        <h1>{item.wine_cat}</h1>
        <ul>
          <li>
            <strong>Actor Name:</strong> {item.country}
          </li>
          <li>
            <strong>Nickname:</strong> {item.price_cat}
          </li>
          <li>
            <strong>Birthday:</strong> {item.rating}
          </li>
        </ul>
      </div>
    </div>
  </div>)
}

export default CharacterItem