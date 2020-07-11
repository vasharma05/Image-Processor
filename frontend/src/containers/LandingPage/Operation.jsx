import React from 'react'
import { Row, Col, Image } from 'react-bootstrap'
import { connect } from 'react-redux'
import * as actions from '../../redux/actions'
import { Button, CircularProgress, Slider } from '@material-ui/core'


function Operation(props){
    const [fetching, setFetching] = React.useState(false)
    const [sliderValue, setSliderValue] = React.useState(1)
    console.log(props)
    const handleOperation = () => {
        setFetching(true)
        props.getFilterImage(props.filter, {
            id: props.id,
            intensity: sliderValue
        })
    }
    if(props[props.filter] && fetching){
        setFetching(false)
    }
    return (
        <Row className='float mx-2 my-2 center-row-center' style={{minWidth: '300px', maxWidth: '100%'}}>
                {!fetching ? 
                    props[props.filter] ? 
                            props[props.filter].map(item => <Image className='mx-3' src={item} width='300px' />)
                    :
                    <Col>
                        {props.slider ? 
                            <Slider
                            valueLabelDisplay='auto'
                            defaultValue={1}
                            onChange={(e, val) => setSliderValue(val)}
                            value={sliderValue}
                            min={1}
                            max = {10}
                            step={1}
                        />:null}
                        <Button color='primary' fullWidth onClick={handleOperation}>
                            {props.filter}
                        </Button>
                    </Col>
                 : <center><CircularProgress color='primary' /></center>}
        </Row>
    )
}

const mapStateToProps = state => ({
    centroid : state.user.centroid,
    gradient : state.user.gradient,
    negative : state.user.negative,
    grayscale : state.user.grayscale,
    segmentation : state.user.segmentation,
    histogram : state.user.histogram,
    average : state.user.average,
    gaussian : state.user.gaussian,
    median : state.user.median,
    sobel : state.user.sobel,

})

const mapDispatchToProps = dispatch => ({
    getFilterImage: (filter, id) => dispatch(actions.getFilterImage(filter, id))
})

export default connect(mapStateToProps, mapDispatchToProps)(Operation)