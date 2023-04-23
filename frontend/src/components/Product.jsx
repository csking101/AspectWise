import React, { useEffect, useState } from 'react'
import { useMatches, useNavigate, useParams } from 'react-router-dom'
import { getReviews } from '../service/productApi'

const PRODUCTS = ["bose","jbl","sony"]
const ASPECTS = ["bass","build","price"]
const SENTIMENTS = ["bad","good"]

const CONFIG = {"bose": {
    "bass" : "bad",
    "build" : "bad",
    "price" : "bad"
},"jbl": {
    "bass" : "bad",
    "build" : "bad",
    "price" : "bad"
},"sony": {
    "bass" : "bad",
    "build" : "bad",
    "price" : "bad"
}}

const isValidProduct = (product) => {
    for (let prod = 0;prod < PRODUCTS.length;prod++){
        if (product.toLowerCase() == PRODUCTS[prod]) {
            return true;
        }
    }

    return false;
}

const Product = () => {
    const { product } = useParams();
    const navigate = useNavigate();

    const [reviews,setReviews] = useState({})

    useEffect(() => {
        if (!isValidProduct(product)) navigate("/")
    })

    useEffect(() => {
        let tempreviews = {}
        for (const aspect in ASPECTS){
            const data = getReviews(product,ASPECTS[aspect],CONFIG[product][ASPECTS[aspect]]);
            tempreviews[ASPECTS[aspect]] = data
        }
        console.log(tempreviews)

        setReviews(tempreviews)
    },[])


  return (
    <div>
        <h1>{product}</h1>
        <h1>Reviews:</h1>
        <table>
            <tr>
                <th>User</th>
                <th>Review</th>
            </tr>
            
        </table>
    </div>
  )
}

export default Product