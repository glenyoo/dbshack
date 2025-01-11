import React from "react";
import { useState } from "react";
import RequestContainer from "../components/RequestContainer";
import RequestForm from "../components/RequestForm";
import Button from "react-bootstrap/Button";
import api from "../httpCommon";

const LandingPage = () => {
  const [addRequest, setAddRequest] = useState(false);

  const fetchData= () => {
    api.post(`/api/token`, { 
        user 
    })
    .then(res => {
      console.log(res);
      console.log(res.data);
    })
  }

  const records = [
    {
      requestDate: "11/01/2025",
      companyName: "Test",
      carbonPrice: "1",
      carbonQuantity: "400",
      requestReason: "Projected excess carbon credits for 2025",
      requestType: "Sell",
    },
    {
      requestDate: "11/01/2025",
      companyName: "Test2",
      carbonPrice: "1",
      carbonQuantity: "600",
      requestReason: "Projected excess carbon credits for 2025",
      requestType: "Sell",
    },
    {
      requestDate: "11/01/2025",
      companyName: "Test3",
      carbonPrice: "1",
      carbonQuantity: "700",
      requestReason: "Projected excess carbon credits for 2025",
      requestType: "Sell",
    },
  ];

  return (
    <>
      {addRequest ? (
        <RequestForm submitText='Add' handleCancel={() => setAddRequest(false)}/>
      ) : (
        <>
          <div className='d-flex justify-content-between'>
            <h1>Welcome Back</h1>
            <Button onClick={() => setAddRequest(true)} variant='info'>
              Add new request
            </Button>
          </div>
          <RequestContainer records={records} />
        </>)
      }
    </>
    )
}

export default LandingPage;
