import React from 'react'
import { Row, Col, Image } from 'react-bootstrap'
import AddToPhotosIcon from '@material-ui/icons/AddToPhotos';
import { FormControl, Button } from '@material-ui/core'
import LibraryAddCheckIcon from '@material-ui/icons/LibraryAddCheck';
import * as actions from '../../redux/actions'
import { connect } from 'react-redux'

function ImageView(props){
    const [uploadedFile, setUploadedFile] = React.useState(null)
    const [uploading, setUploading] = React.useState(false)
    const handleImageSubmit = (e) => {
        let form = new FormData()
        form.append('image', uploadedFile, uploadedFile.name)
        props.uploadImage(form)
        setUploading(true)
    }
    if(props.image && uploading){
        setUploading(false)
        props.setCurrentImage({
            id: props.imageId,
            image: props.image
        })
    }
    const handleReset = () =>{
        props.setCurrentImage(null)
        props.resetImage()
    }
    return (
        <Row className='center-row-center mt-4'>
                <div className='p-3 float center-col-center text-center img-ctn' style={{maxWidth:'100%', minWidth: '200px',}}>
                        {props.currentImage ? 
                        <>
                            <Image src={props.currentImage.image} style={{maxWidth:'100%', maxHeight: '300px', borderRadius:'16px'}} />
                            <Row className='mt-3'>
                                <Col className='end-col'>
                                    <Button color='primary' className='ml-auto' onClick={handleReset}>Add another Image</Button>      
                                </Col>
                            </Row>
                        </>
                        :
                            <div style={{width:'100%'}}>
                                <FormControl>
                                    <label htmlFor='uploadFile'>
                                        {!uploadedFile ? <AddToPhotosIcon className='add-icon' style={{color: '#9400D3', fontSize:'40px'}} /> : <LibraryAddCheckIcon style={{color:'green', fontSize: '40px'}} />}
                                    </label>
                                    <input
                                        type='file'
                                        accept='image/*'
                                        id='uploadFile'
                                        onChange={(e) => setUploadedFile(e.target.files[0])}
                                        style={{
                                            display: 'none'
                                        }}
                                    />
                                </FormControl>
                                <h6 className='mt-3'>{uploadedFile ? uploadedFile.name : 'Add an image to start'}</h6>
                                {uploadedFile ? 
                                    <Row className='mt-3 center-row-around'>
                                        <Button variant='oultined' onClick={() => setUploadedFile(null)}>Cancel</Button>
                                        <Button variant='oultined' color='primary' onClick={handleImageSubmit} >Add</Button>
                                    </Row>
                                : null}
                            </div>
                        }
                </div>
            </Row>
    )
}
const mapStateToProps = state => ({
    image: state.user.image,
    imageId: state.user.imageId
})

const mapDispatchToProps = dispatch => ({
    uploadImage: (payload) => dispatch(actions.uploadImage(payload)),
    resetImage: () => dispatch(actions.resetImage())
})
export default connect(mapStateToProps, mapDispatchToProps)(ImageView)