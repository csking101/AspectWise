import React, { useEffect, useState } from 'react'
import { useMatches, useNavigate, useParams } from 'react-router-dom'
import { getReviews } from '../service/productApi'

const PRODUCTS = ["bose","jbl","sony"]
const ASPECTS = ["bass","build","price"]
const SENTIMENTS = ["bad","good"]

const CONFIG = {"bose": {
    "bass" : "good",
    "build" : "good",
    "price" : "good"
},"jbl": {
    "bass" : "good",
    "build" : "good",
    "price" : "good"
},"sony": {
    "bass" : "good",
    "build" : "good",
    "price" : "good"
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

    const [reviews,setReviews] = useState({"bass":[],"build":[],"price":[]})
    const [imgUrl,setImgUrl] = useState("")

    useEffect(() => {
        if (!isValidProduct(product)) navigate("/")

        setImgUrl("../resources/images/"+product+"1.jpg")
    },[])

    useEffect(() => {
        if (isValidProduct(product)){
        setReviews({"bass":[],"build":[],"price":[]})
        console.log(reviews)
        console.log("Change in product")

        for (const aspect in ASPECTS){
            const data = getReviews(product,ASPECTS[aspect],CONFIG[product][ASPECTS[aspect]])
                        .then((resData) => {
                            let tempObj = {[ASPECTS[aspect]]:resData}

                            setReviews((prevReviews) => ({
                                ...prevReviews,
                                ...tempObj
                            }))
                            console.log(tempObj)
                        })
        }}
    },[product])


  return (
    <div>
        <h1>{product}</h1>
        {imgUrl?
        <img src={require("../resources/images/"+product+"1.jpg")}
                        alt="logo"
                        onerror={() => {
                                alert('invalid img')
                            }
                        }
                  /> : null
        }
        {ASPECTS.map((aspect,idx) => {
            return (
                <div>
                    <h1>Reviews:{aspect}</h1>
                    <table>
                        <tr>
                            <th>User</th>
                            <th>Review</th>
                        </tr>
                        {reviews[aspect].map((review,idx) => {
                            return (<tr>
                                <td>{idx+1}</td>
                                <td>{review}</td>
                            </tr>)
                        })}
                    </table>
                </div>
            )
        })}
    </div>
  )
}

export default Product