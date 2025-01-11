import React from 'react'

const Request = ({ requestDate, companyName, carbonPrice, carbonQuantity, requestReason, requestType}) => {
  return (
    <tr>
        <td>1</td>
        <td>{requestDate}</td>
        <td>{companyName}</td>
        <td>{carbonPrice}</td>
        <td>{carbonQuantity}</td>
        <td>{requestReason}</td>
        <td>{requestType}</td>
    </tr>
  )
}

export default Request