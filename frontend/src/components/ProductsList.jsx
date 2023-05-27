import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getProducts } from '../service/productApi'
import NavBar from './NavBar'

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
      <NavBar></NavBar>
      <center><h1 style={{ color:'#B71375'}}>List of Products</h1></center>
      <div style={{ display:'flex',justifyContent:'space-around',margin:'4vh' }}>
      {products.length?
      products.map((product) => {
        return (<div style={{ }}>
                  <Link to={"/product/"+product} style={{ textDecoration:'none',color:"#FC4F00" }}>
                  <center><h2>{product.toUpperCase()}</h2></center>
                  <img src={require("../resources/images/"+product+"1.jpg")}
                        alt="logo"
                        height={300}
                        width={300}
                  />
                  </Link>
                </div>
        )
      }) :<p>LOADING</p> }
      </div>
    </div>
  )
}

export default ProductsList