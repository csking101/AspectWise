import React from 'react'
import { Link } from "react-router-dom";
import { Paper, Typography } from '@mui/material';
import { styled } from '@mui/system';

const pages = ["Home","Products"]

const NavBarItem = styled('div')`
  padding: 3vh;
  margin: 0vh;
  text-align: center;
`;

const NavBarDiv = styled(Paper)`

  elevation: 10;
  position: sticky;
  display: flex;
  direction: horizontal;
`;

const NavBarItemText = styled(Typography)`
  
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