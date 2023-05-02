import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import Home from './components/Home';
import ProductsList from './components/ProductsList';
import Product from './components/Product';
import NotFound from './components/NotFound';
import './index.css';
import NavBar from './components/NavBar';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route path="" element={<Home />} />
      <Route path="home" element={<Home />} />
      <Route path="products" element={<ProductsList />} />
      <Route path="product/:product" element={<Product />} />
    </Route>
  )
);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);