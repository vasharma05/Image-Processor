import React from 'react'
import { connect } from 'react-redux'
import { Dialog, DialogTitle, DialogContent } from '@material-ui/core'
import * as actions from '../../redux/actions'

function NetworkError(props) {
    return (
        <Dialog
            open={props.networkError}
            onClose={() => props.retry()}
        >
            <DialogTitle>Network Error</DialogTitle>
            <DialogContent>
                <p>Can't connect to server</p>
            </DialogContent>
        </Dialog>
    )
}
const mapStateToProps = (state)=> {
    return {
        networkError: state.auth.networkError
    }
}
const mapDispatchToProps = (dispatch) => ({
    retry: () => dispatch(actions.retryConnection())
})
export default connect(mapStateToProps, mapDispatchToProps)(NetworkError)
