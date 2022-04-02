import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CharacterGrid from '../Filter/CharacterGrid';
import Search from '../Filter/Search';
import './Wine.css';



function Wine(){

  const [items, setItems] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [query, setQuery] = useState('')

useEffect(() => {
  const fetchItems = async () => {
    setIsLoading (true)
    var URL = 'http://localhost:5000/testdata'
    if (query !==""){
       URL = `http://localhost:5000/origin/${query}`
    }
    const result = await axios(
      URL
      ) 

    // console.log(result.data)
    setItems (result.data)
    setIsLoading(false)
  }

fetchItems ()
}, [query])


  return (
    <div className="container">
      <br></br>
    <h1 style={
      { color: "#5E2028",
      textAlign: "center"}}>Let's find the wine.</h1>
  

      <Search getQuery={(q) => setQuery(q)} />
      <CharacterGrid isLoading = {isLoading} items={items}/> 
    </div>
  );
}


export default Wine;