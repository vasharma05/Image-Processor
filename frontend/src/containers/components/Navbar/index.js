import React from 'react'
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'
import { withRouter, Redirect } from 'react-router-dom'

const Navbar = (props) => {
    const [redirect, setRedirect] = React.useState(false)
    const handleLogout = () => {
        console.log(props.history)
        window.localStorage.removeItem('persist:rootReducer')
        setRedirect(true)
    }
    console.log(redirect)
    return ( 
        redirect ? <Redirect to='/signin' /> :
        <nav className="navbar navbar-expand-lg navbar-light bg-dark py-2">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <Link to='/'>Navbar</Link>

            <div className="collapse navbar-collapse" id="navbarTogglerDemo03">
                
                    {props.signinData ?
                        <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
                            <li className="nav-item ml-3">
                                <Link to='/messages' >Dashboard</Link>
                            </li>
                            <li className="nav-item ml-3">
                                <span style={{color:'blue'}}>{props.userDetails.username}</span>
                            </li>
                            <li className="nav-item ml-3">
                                <span style={{color:'blue'}} onClick={handleLogout}>Logout</span>
                            </li>
                        </ul>
                    : 
                        <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
                            <li className="nav-item ml-3">
                                <Link to='/signin'>Sign In</Link>
                            </li>
                            <li className="nav-item ml-3">
                                <Link to='/signup'>Sign Up</Link>
                            </li>
                        </ul>
                    }
            </div>
        </nav>
    )
}

const mapStateToProps = (state) => ({
    signinData: state.auth.signinData, 
    userDetails: state.auth.userDetails
})
export default connect(mapStateToProps)(withRouter(Navbar))