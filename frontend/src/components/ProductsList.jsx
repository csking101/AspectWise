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
        return (
          <h2>{product}</h2>
        )
      }) :<p>LOADING</p> }
    </div>
  )
}

export default ProductsList