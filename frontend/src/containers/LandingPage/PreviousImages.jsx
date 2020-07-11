import React from 'react'
import { Row, Col, Image } from 'react-bootstrap'
import { CircularProgress, Drawer } from '@material-ui/core'

function PreviousImage(props){
    return (
        <Drawer open={props.openDrawer} anchor={"right"} onClose={() => props.setOpenDrawer(false)} >
            <Row className='mt-2'>
                <Col className='text-center'><h6>Your Previous Images used</h6></Col>
            </Row>
            <Row className='mt-3'>
                <Col>
                    {props.imageList ? 
                    props.imageList.length > 0 ? props.imageList.map(item => {
                        return (
                            <Row className='mt-3 p-2 center-row' onClick={() => props.setCurrentImage(item)} style={{borderBottom: '1px solid grey', cursor:'pointer'}}>
                                    <Image src={item.image} height='50px' />
                                    <span className='ml-2'>{item.image.substring(35,)}</span>
                            </Row>
                        )
                    }) : 'No images found.'
                : <center className='mt-3'><CircularProgress color='primary' /></center>}
                    </Col>
            </Row>
        </Drawer>
    )
}

export default PreviousImage