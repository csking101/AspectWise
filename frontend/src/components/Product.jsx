import React, { useEffect, useState } from 'react'
import { useMatches, useNavigate, useParams } from 'react-router-dom'
import { getReviews } from '../service/productApi'
import { styled } from '@mui/system';
import NavBar from './NavBar'
import { Typography } from '@mui/material';

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

const ProductDescriptionBox = styled('div')`
    margin-left:2vw;
`;

const ProductInformation = styled('div')`
    margin-left:2vw;
    margin-top:3vh;
    display:flex;
`;



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
        <NavBar></NavBar>
        <ProductInformation>
        {imgUrl?
        <img src={require("../resources/images/"+product+"1.jpg")}
                        alt="logo"
                        onerror={() => {
                                alert('invalid img')
                            }
                        }
                height={300}
                width={300}
                  /> : null
        }
        <ProductDescriptionBox>
        <h1>{product.toUpperCase()} 821C with Bluetooth 5.0 and Voice Assistant Support </h1>
        <p>3.0/5.0<p style={{ color:"yellow",display:"inline" }}> &nbsp;★★★☆☆</p> 15,921 ratings | 421 reviews</p>
        <p><a href="google.com" style={{ textDecoration:'none' }}>Go to the bose site</a></p>
        <hr style={{ border:'none',borderBottom:'1px solid' }}/>
        <h3><s>₹9999.00</s>&nbsp;₹6969.00</h3>
        <p>Inclusive of all taxes</p>
        <hr style={{ border:'none',borderBottom:'1px solid' }}/>
        <div style={{ display:'flex' }}>
            {
                ["Free Delivery","Pay on Delivery","7 Days Replacement","1 Year Warranty","Top Brand"].map((data) => {
                    return (<div style={{ border:"2px solid",padding:"5px",margin:"4px" }}>
                        {data}
                    </div>)
                })
            }
        </div>

        
        </ProductDescriptionBox>
        </ProductInformation>
        {ASPECTS.map((aspect,idx) => {
            return (
                <div>
                    <h1>Reviews about {aspect}</h1>
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