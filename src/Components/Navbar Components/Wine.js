import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CharacterGrid from '../Filter/CharacterGrid';
import Search from '../Filter/Search';
import './Wine.css';

/*
const App = () => {
  const [items, setItems] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [query, setQuery] = useState('')

useEffect(() => {
  const fetchItems = async () => {
    setIsLoading (true)
    const result = await axios(
      `http://localhost:5000/alldata=${query}`
      ) 

    // console.log(result.data)
    setItems (result.data)
    setIsLoading(false)
  }

fetchItems ()
}, [query])*/

function Wine() {

  const [data, setData] = useState({})
	const [items, setItems] = useState([])
  	const [isLoading, setIsLoading] = useState(true)
  	const [query, setQuery] = useState('')

useEffect(() => {
		
  fetch("http://localhost:5000/alldata").then(
    res => res.json()
    ).then(data => {
        setData(data)
        console.log(data)
        
          setIsLoading(false)
      }
    )
  
}, [])

  return (
    <div className="container">
      <br></br>
    <h1 style={
      { color: "#5E2028",
      textAlign: "center"}}>Let's find the wine.</h1>
  
/*
      <Search getQuery={(q) => setQuery(q)} />
      <CharacterGrid isLoading = {isLoading} items={items}/> 
    </div>
  );
}

export default Wine;