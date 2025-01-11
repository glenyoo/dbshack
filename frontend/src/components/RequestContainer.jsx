import React from 'react'
import { useLocation } from 'react-router-dom';
import Request from './Request';
import Table from 'react-bootstrap/Table';

const RequestContainer = ({ records }) => {
    const {pathname} = useLocation()

  return (
    <>
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
        {records.map((request, index) => 
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