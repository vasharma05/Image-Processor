import React from 'react'
import { Row, Col} from 'react-bootstrap'
import Operation from './Operation'

export default function ApplyOperations(props){
    
    return (
        <>
            <Row className='mt-3'>
                <Col>
                    <h2>Apply the operations given below!</h2>
                </Col>
            </Row>
            <Row className='mt- center-row-around'>
                <Operation id={props.currentImage.id} filter='centroid' />
                <Operation id={props.currentImage.id} filter='gradient' />
                <Operation id={props.currentImage.id} filter='negative' />
                <Operation id={props.currentImage.id} filter='grayscale' />
                <Operation id={props.currentImage.id} filter='segmentation' />
                <Operation id={props.currentImage.id} filter='histogram' />
                <Operation id={props.currentImage.id} slider={true} filter='average' />
                <Operation id={props.currentImage.id} filter='gaussian' />
                <Operation id={props.currentImage.id} slider={true} filter='median' />
                <Operation id={props.currentImage.id} filter='sobel' />
            </Row>
        </>
    )
}



