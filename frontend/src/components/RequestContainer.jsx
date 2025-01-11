import React from 'react'
import Table from 'react-bootstrap/Table';

const RequestContainer = () => {
    const data = [
        {
            requestDate: "11/01/2025",
            companyName: "Test",
            createdDatetime: "11/01/2025 09:01:00",
            carbonPrice: "1",
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
        </tr>
      </thead>
      <tbody>
      </tbody>
    </Table>
    </>
  )
}

export default RequestContainer