import React, { Component } from 'react'
import { Row, Col } from 'react-bootstrap'
import { Input , Button, FormControl, InputLabel, CircularProgress } from '@material-ui/core'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux'
import * as actions from '../../redux/actions'
import Navbar from '../components/Navbar'

export class SignInView extends Component {
    constructor(){
        super()
        this.state = {
            username: '', 
            password: ''
        }
        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleChange = this.handleChange.bind(this)
    }
    handleSubmit(e){
        e.preventDefault()
        console.log('Submitted')
        this.props.login(this.state)
    }
    handleChange(e){
        this.setState({
            [e.target.name]: e.target.value
        })
    }
    render() {
        return (
            <div className='parent'>
                    <Navbar />
                    <Row>
                        <Col className='col-md-6 offset-md-3'>
                            <Row className='mt-5 box p-3'>
                                <Col>
                                    {this.props.authError ? <span style={{color: 'red'}}>{this.props.authError}</span>: null}
                                    <h1 className='mt-3'>Sign In</h1>
                                    <Row>
                                        <Col>
                                            <form onSubmit={this.handleSubmit} className='mt-3' style={{width: '100%'}}>
                                                <FormControl fullWidth>
                                                    <InputLabel>Username</InputLabel>
                                                    <Input
                                                        value={this.state.username}
                                                        onChange = {this.handleChange}
                                                        name='username'
                                                        required={true}
                                                        fullWidth={true}
                                                        variant='Outlined'
                                                    />
                                                </FormControl>
                                                <FormControl className='mt-3' fullWidth>
                                                    <InputLabel>Password</InputLabel>
                                                    <Input
                                                        type='password'
                                                        value={this.state.password}
                                                        onChange = {this.handleChange}
                                                        name='password'
                                                        required={true}
                                                        fullWidth={true}
                                                        variant='Outlined'
                                                    />
                                                </FormControl>
                                                {this.props.authLoading ? <CircularProgress className='mt-4' color='primary' /> : <Button className='mt-4' type='submit' variant='contained' color='primary'>Submit</Button>}
                                            </form>
                                            <Row>
                                                <Col className='mt-2'>
                                                    <span className='small ml-auto'>New User? Please Register yourself <Link to='/signup'>here</Link></span>
                                                </Col>
                                            </Row>
                                        </Col>
                                    </Row>
                                </Col>
                            </Row>
                        </Col>
                    </Row>
            </div>
        )
    }
}
const mapStateToProps = (state) => ({
    authError: state.auth.authError,
    authLoading: state.auth.authLoading,
    signinData : state.auth.signinData
})

const mapDispatchToProps = (dispatch) => ({
    login: (payload) => dispatch(actions.login(payload))
})
export default connect(mapStateToProps, mapDispatchToProps)(SignInView)
