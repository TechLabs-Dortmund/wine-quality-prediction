import React from 'react'

const CharacterItem = ({item}) => {
  console.log(item)
    return ( 
    <div className='cardSearch'>
    <div className='cardSearch-inner'>
      <div className='cardSearch-front'>
        <img src={"https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2787&q=80"} alt='' />
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