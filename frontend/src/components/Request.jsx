import React from 'react'
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const Request = ({ requestId, requestDate, companyName, carbonPrice, carbonQuantity, requestReason, requestType, handleEdit, handleDelete}) => {
    const navigate = useNavigate();
    const {pathname} = useLocation();
    const [isDelete, setIsDelete] = useState(false);

    const navigateEdit = () => {
        navigate(`/edit/${requestId}`)
    }

    return (
    <tr>
        <td>1</td>
        <td>{requestDate}</td>
        <td>{companyName}</td>
        <td>{carbonPrice}</td>
        <td>{carbonQuantity}</td>
        <td>{requestReason}</td>
        <td>{requestType}</td>
        {pathname === '/home' && (
            !isDelete ?
            <td>
                <Button onClick={() => navigateEdit()} variant="primary">Edit</Button>
                <Button onClick={() => {setIsDelete(true)}} variant="danger">Delete</Button>
            </td> :
            <td>
                <Button onClick={handleDelete} variant="dark">Confirm</Button>
                <Button onClick={() => {setIsDelete(false)}} variant="secondary">Cancel</Button>
            </td>
        )}
    </tr>
  )
}

export default Request