import React, { useEffect } from 'react'
import { useMatches, useNavigate, useParams } from 'react-router-dom'

const VALID_PRODUCTS = ["jbl","sony","bose"]

const isValidProduct = (product) => {
    for (let prod = 0;prod < VALID_PRODUCTS.length;prod++){
        if (product.toLowerCase() == VALID_PRODUCTS[prod]) {
            return true;
        }
    }

    return false;
}

const Product = () => {
    const { product } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        if (!isValidProduct(product)) navigate("/")
    })

  return (
    <div>
        <h1>{product}</h1>
        <p>Hello</p>
    </div>
  )
}

export default Product