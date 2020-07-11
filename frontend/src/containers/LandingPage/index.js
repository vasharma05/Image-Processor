import React from 'react'
import { Row, Col } from 'react-bootstrap'
import { withRouter } from 'react-router-dom'
import './landingPage.css'
import { Button } from '@material-ui/core'
import ImageView from './ImageView'
import { connect } from 'react-redux'
import ApplyOperations from './ApplyOperations'
import PreviousImages  from './PreviousImages'
import * as actions from '../../redux/actions'

function LandingPage(props){
    // States
    const [currentImage, setCurrentImage] = React.useState(null)
    const [fetchingList, setFetchingList] = React.useState(true)
    const [imageList, setImageList] = React.useState(props.imageList)
    const [openDrawer, setOpenDrawer] = React.useState(false)
    React.useEffect(()=>{
        props.fetchUserImages()
    }, [])
    if(props.imageList && fetchingList){
        setFetchingList(false)
        setImageList(props.imageList)
    }
    return(
        <>
            <Row className='header'>
                <Col className='py-2'>
                    <h3>Term Project</h3>
                </Col>
                <div>
                    <Button color='primary' onClick={() => setOpenDrawer(true)} >Previous Images</Button>
                </div>
            </Row>
            <ImageView currentImage={currentImage} setCurrentImage={setCurrentImage} />
            <PreviousImages openDrawer={openDrawer} setOpenDrawer={setOpenDrawer} imageList={imageList} setCurrentImage={setCurrentImage} />
            {currentImage ? <ApplyOperations currentImage={currentImage} /> : null}
        </>
    )
}

const mapStateToProps = state => ({
    imageList: state.user.imageList
})

const mapDispatchToProps = dispatch => ({
    fetchUserImages: () => dispatch(actions.fetchUserImages())
})

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(LandingPage))