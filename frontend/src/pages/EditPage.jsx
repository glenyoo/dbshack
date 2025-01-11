import React from 'react'
import { useParams } from "react-router-dom";
import RequestForm from '../components/RequestForm';

const EditPage = () => {
    const { requestId } = useParams();
  
return (
    <RequestForm requestId={requestId} submitText="Edit"/>
  )
}

export default EditPage