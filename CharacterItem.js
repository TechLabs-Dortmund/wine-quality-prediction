import React from 'react'

const CharacterItem = ({item}) => {
  console.log(item)
    return ( 
    <div className='cardSearch'>
    <div className='cardSearch-inner'>
      <div className='cardSearch-front'>
        <img src={item.img} alt='' />
      </div>
      <div className='cardSearch-back'>
        <h5>{item.title}</h5>
        <ul>
          <li>
            <strong>Region:</strong> {item.country}
          </li>
          <li>
            <strong>Price:</strong> {item.price_cat}
          </li>
          <li>
            <strong>Rating:</strong> {item.rating}
          </li>
        </ul>
      </div>
    </div>
  </div>)
}

export default CharacterItem