import React from 'react'
import './temp.css'


const RatingTable = () => {

  return (
    <div>
      <center>
        <h1>From the Recommender System:</h1>
      <table>
        <tr>
          <th>Brand</th>
          <th>Audio</th>
          <th>Build</th>
          <th>Price</th>
        </tr>

        <tr>
          <td>Sony</td>
          <td>2.313496726044154</td>
          <td>-0.32487670045632583</td>
          <td>0.44484699623925344</td>
        </tr>

        <tr>
          <td>Bose</td>
          <td>1.899477267033094</td>
          <td>-1.1481827867906647</td>
          <td>1.950780949706123</td>
        </tr>

        <tr>
          <td>JBL</td>
          <td>0.3183155100764209</td>
          <td>0.6265267612559072</td>
          <td>0.2904070736071385</td>
        </tr>
      </table>

      <div>
        <h2>Best Audio: Sony &gt; Bose &gt; JBL</h2>
        <h2>Best Build: JBL &gt; Sony &gt; Bose</h2>
        <h2>Best Price: Bose &gt; Sony &gt; JBL</h2>
      </div>

      </center>
    </div>
  )
}

export default RatingTable