import React from 'react'
import { useMatches, useParams } from 'react-router-dom'

const Product = () => {
    const { product } = useParams();


  return (
    <div>
        <h1>{product}</h1>
        <p>Hello</p>
    </div>
  )
}

export default Product