import React from 'react'
import { Link } from "react-router-dom";
import { Paper, Typography } from '@mui/material';
import { styled } from '@mui/system';

const pages = ["Home","Products"]

const NavBarItem = styled('div')`
  padding: 3vh;
  margin: 0vh;
  text-align: center;
  background-color: #8B1874;
`;

const NavBarDiv = styled(Paper)`
  background-color: #8B1874;
  elevation: 10;
  position: sticky;
  display: flex;
  direction: horizontal;
  color: #2CD3E1;
`;

const NavBarItemText = styled(Typography)`
  background-color: #8B1874;
  color: #2CD3E1;
  text-decoration: none;
  
`;


const NavBar = () => {
  return (
    <NavBarDiv>
      {pages.map((item) => {
        return (
          <Link to={'/'+item} style={{ textDecoration: 'none' }}>
          <NavBarItem>
            <NavBarItemText>
              {item}
            </NavBarItemText>
          </NavBarItem>
          </Link>
        )
      })}
    </NavBarDiv>
  )
}

export default NavBar