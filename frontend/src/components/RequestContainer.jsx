import React from 'react'
import { useLocation } from 'react-router-dom';
import Request from './Request';
import Table from 'react-bootstrap/Table';

const RequestContainer = () => {
    const {pathname} = useLocation()

    const data = [
        {
            requestDate: "11/01/2025",
            companyName: "Test",
            carbonPrice: "1",
            carbonQuantity: "400",
            requestReason: "Projected excess carbon credits for 2025",
            requestType: "Sell"
        },
        {
            requestDate: "11/01/2025",
            companyName: "Test2",
            carbonPrice: "1",
            carbonQuantity: "600",
            requestReason: "Projected excess carbon credits for 2025",
            requestType: "Sell"
        },
        {
            requestDate: "11/01/2025",
            companyName: "Test3",
            carbonPrice: "1",
            carbonQuantity: "700",
            requestReason: "Projected excess carbon credits for 2025",
            requestType: "Sell"
        }
    ]

  return (
    <>
        <div>Outstanding Requests</div>
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>#</th>
          <th>Request Date</th>
          <th>Company Name</th>
          <th>Carbon Price (SGD/Tonnes)</th>
          <th>Carbon Quantity</th>
          <th style={{width: '600px'}}>Requesting Reason</th>
          <th>Request Type</th>
          {pathname === '/home' && <th style={{width: '300px'}}>Edit/Delete</th>}
        </tr>
      </thead>
      <tbody>
        {data.map((request, index) => 
            <Request
                key = {index}
                requestDate = {request.requestDate}
                companyName = {request.companyName}
                carbonPrice = {request.carbonPrice}
                carbonQuantity = {request.carbonQuantity}
                requestReason = {request.requestReason}
                requestType = {request.requestType}
            />
        )}
      </tbody>
    </Table>
    </>
  )
}

export default RequestContainer