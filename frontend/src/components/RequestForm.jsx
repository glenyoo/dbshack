import { useState } from "react";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";
import Button from 'react-bootstrap/Button';

const RequestForm = (handleOnClick) => {
  const [requestDate, setRequestDate] = useState("");
  const [companyName, setCompanyName] = useState("");
  const [carbonPrice, setCarbonPrice] = useState(0);
  const [carbonQuantity, setCarbonQuantity] = useState(0);
  const [requestType, setRequestType] = useState("sell");
  const [requestReason, setRequestReason] = useState("");

  return (
    <Form>
      <Form.Group as={Row} className='mb-3' controlId='formPlaintextPassword'>
        <Form.Label column sm='2'>
          Request Date
        </Form.Label>
        <Col sm='10'>
          <Form.Control
            type='date'
            value={requestDate}
            onChange={(e) => setRequestDate(e.target.value)}
            placeholder='Request Date'
          />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className='mb-3'>
        <Form.Label column sm='2'>
          Company Name
        </Form.Label>
        <Col sm='10'>
          <Form.Control
            value={companyName}
            onChange={(e) => setCompanyName(e.target.value)}
            placeholder='Company Name'
          />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className='mb-3'>
        <Form.Label column sm='2'>
          Carbon Price
        </Form.Label>
        <Col sm='10'>
          <Form.Control
            type='number'
            value={carbonPrice}
            onChange={(e) => setCarbonPrice(e.target.value)}
            placeholder='Carbon Price'
          />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className='mb-3'>
        <Form.Label column sm='2'>
          Carbon Quantity
        </Form.Label>
        <Col sm='10'>
          <Form.Control
            type='number'
            value={carbonQuantity}
            onChange={(e) => setCarbonQuantity(e.target.value)}
            placeholder='Carbon Quantity'
          />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className='mb-3'>
        <Form.Label>Carbon Type</Form.Label>
        <Form.Select
          value={requestType}
          onChange={(e) => setRequestType(e.target.value)}
          aria-label='Default select example'
        >
          <option value='buy'>Buy</option>
          <option value='sell'>Sell</option>
        </Form.Select>
      </Form.Group>

      <Form.Group className='mb-3' controlId='exampleForm.ControlTextarea1'>
        <Form.Label>Request Reason</Form.Label>
        <Form.Control
          value={requestReason}
          onChange={(e) => setRequestReason(e.target.value)}
          as='textarea'
          rows={3}
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Add
      </Button>
    </Form>
  );
};

export default RequestForm;
