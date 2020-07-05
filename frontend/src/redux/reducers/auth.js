const initState = {
    authError: null,
    authLoading: false,
    signinData: null,
    userDetails: null, 
    networkError : false
}

const updateObject = (state, newState) => ({
    ...state, 
    ...newState
})

const userAuthStart = (state, action) => 
    updateObject(state, {
        authLoading:true,
        networkError: false
    })

const userAuthError = (state, action) => 
    updateObject(state, {
        authError: action.error,
        authLoading: false
    })

const userAuthSuccess = (state, action) => 
    updateObject(state, {
        signinData: action.payload.token,
        userDetails: action.payload.userDetails,
        authLoading: false,
        authError: null
    })


const networkError = (state, action) => 
    updateObject(state, {
        networkError: true,
        authLoading: false
    })

const retryConnection = (state, action) => 
    updateObject(state, {
        networkError : false
    })

const authReducer = (state=initState, action) => {
    switch(action.type){
        case 'RETRY_CONNECT':
            return retryConnection(state, action)
        case 'USER_AUTH_START':
            return userAuthStart(state, action)
        case 'USER_AUTH_ERROR':
            return userAuthError(state, action)
        case 'USER_AUTH_SUCCESS':
            return userAuthSuccess(state, action)
        case 'NETWORK_ERROR':
            return networkError(state, action)
        default: 
            return state
    }
}

export default authReducer