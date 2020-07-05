import React, { Component } from 'react'
import {Row, Col} from 'react-bootstrap'
import { FormControl, TextField, Button, CircularProgress } from '@material-ui/core'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux'
import * as actions from '../../redux/actions'
import Navbar from '../components/Navbar'

export class SignupView extends Component {
    constructor(){
        super()
        this.state = {
            first_name: '',
            last_name: '',
            email: '',
            username: '',
            password: '',
            confirmPassword: '',
            passwordMismatch: false
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }
    handleChange(e){
        if(e.target.name === 'profile_pic'){
            this.setState({
                profile_pic: e.target.files[0]
            }, ()=> console.log(this.state.profile_pic))
            return
        }
        this.setState({
            [e.target.name]: e.target.value
        }, ()=>{
            if(this.state.password !== this.state.confirmPassword){
                this.setState({
                    passwordMismatch: true
                })
            }else{
                this.setState({
                    passwordMismatch: false
                })
            }
        })
    }
    handleSubmit(e){
        e.preventDefault()
        let formData = new FormData()
        for(let key in this.state){
            console.log(key, this.state[key])
            if(key === 'profile_pic'){
                if(this.state[key]){
                    formData.append(key, this.state[key], this.state[key].name)
                }
            }else{
                formData.append(key, this.state[key])
            }
        }
        this.props.signup(formData)
    }
    render() {
        return (
            <div className='parent'>
                <Navbar />
                <Row className='mt-5'>
                    <Col className='col-md-6 offset-md-3 box p-3'>
                    {this.props.authError ? <span style={{color: 'red'}}>{this.props.authError}</span>: null}
                        <form className='mt-4' onSubmit={this.handleSubmit}>
                            <h1>Sign Up</h1>
                            <Row className='mt-4'>
                                <Col>
                                    <FormControl fullWidth>
                                        <TextField
                                            variant='outlined'
                                            value={this.state.first_name}
                                            onChange={this.handleChange}
                                            name='finame'
                                            label='Name'
                                            color='primary'
                                            required
                                        />
                                    </FormControl>
                                </Col>
                            </Row>
                            <Row className='mt-3'>
                                <Col>
                                    <FormControl fullWidth>
                                        <TextField
                                            variant='outlined'
                                            type='email'
                                            value={this.state.email}
                                            onChange={this.handleChange}
                                            name='email'
                                            label='Email'
                                            color='primary'
                                            required
                                        />
                                    </FormControl>
                                </Col>
                            </Row>
                            <Row className='mt-3'>
                                <Col>
                                    <FormControl fullWidth>
                                        <TextField
                                            variant='outlined'
                                            value={this.state.username}
                                            onChange={this.handleChange}
                                            name='username'
                                            label='Username'
                                            color='primary'
                                            required
                                        />
                                    </FormControl>
                                </Col>
                            </Row>
                            <Row className='mt-3'>
                                <Col>
                                    <FormControl fullWidth>
                                        <TextField
                                            variant='outlined'
                                            type='password'
                                            value={this.state.password}
                                            onChange={this.handleChange}
                                            name='password'
                                            label='Password'
                                            color='primary'
                                            error={this.state.passwordMismatch}
                                            required
                                        />
                                    </FormControl>
                                </Col>
                            </Row>
                            <Row className='mt-3'>
                                <Col>
                                    <FormControl fullWidth>
                                        <TextField
                                            variant='outlined'
                                            type='password'
                                            value={this.state.confirmPassword}
                                            onChange={this.handleChange}
                                            name='confirmPassword'
                                            label='Confirm Password'
                                            color='primary'
                                            error={this.state.passwordMismatch}
                                            required
                                        />
                                    </FormControl>
                                </Col>
                            </Row>
                            <Row className='mt-4'>
                                <Col>
                                {this.props.authLoading ? <CircularProgress color='primary' /> : <Button className='mt-4' type='submit' variant='contained' color='primary' disabled={this.state.passwordMismatch}>Sign Up</Button>}

                                </Col>
                            </Row>
                        </form>
                        <Row className='mt-4'>
                            <Col>
                                <span className='ml-auto small'>Already an user? Sign in <Link to='/signin'>here</Link></span>
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
    signinData : state.auth.signinData,
    authLoading : state.auth.authLoading
})
const mapDispatchToProps = (dispatch)=>({
    signup : (payload) => dispatch(actions.signup(payload))
})
export default connect(mapStateToProps, mapDispatchToProps)(SignupView)
