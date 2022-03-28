import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CharacterGrid from '../Filter/CharacterGrid';
import Search from '../Filter/Search';
import './Wine.css';



function Wine() {
	// usestate for setting a javascript
	// object for storing and using data
	/*const [data, setdata] = useState({
		wine_cat: "",
		country: 0,
		price_cat: "",
		rating: "",
	});

	// Using useEffect for single rendering
	useEffect(() => {
		// Using fetch to fetch the api from
		// flask server it will be redirected to proxy
		fetch("/Backend/data").then((res) =>
			res.json().then((data) => {
				// Setting a data from api
				setdata({
					wine_cat: data.wine_cat,
					country: data.country,
					price_cat: data.price_cat,
					rating: data.rating,
				});
			})
		);
	}, []); */

	return (
		<div className="container">
			
				<h1>React and flask</h1>
				
			
      	

			
		</div>
	);
}

export default Wine;




/*
const Wine = () => {
  const [items, setItems] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [query, setQuery] = useState('')

useEffect(() => {
  const fetchItems = async () => {
    setIsLoading (true)
    const result = await axios(
      `http://localhost:5000${query}`
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

export default Wine;*/