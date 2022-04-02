import React from 'react'
import CharacterItem from './CharacterItem';
import Spinner from './Spinner';

const CharacterGrid = ({items, isLoading}) => {
    
    return isLoading ? 
    <Spinner />
     : 
    <section className="cards">
        {Object.entries(items).map((item) =>(
            <CharacterItem key={item[0]} item={item[1]}></CharacterItem>
        ))}
    </section>
}

export default CharacterGrid