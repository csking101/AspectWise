import React, { useEffect, useState } from 'react'
import { getProducts } from '../service/productApi'

const ProductsList = () => {
  const [products,setProducts] = useState([])

  useEffect(() => {
    const data = getProducts()
                 .then((resData) => {
                  setProducts(resData)
                 })
  },[])

  return (
    <div>
      <h1>List of Products</h1>
      {products.length?
      products.map((product) => {
        return (<div>
                  <h2>{product}</h2>
                  <img src={require("../resources/images/"+product+"1.jpg")}
                        alt="logo"
                  />
                  
                </div>
        )
      }) :<p>LOADING</p> }
    </div>
  )
}

export default ProductsList