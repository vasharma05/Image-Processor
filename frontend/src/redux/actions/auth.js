import * as types from '../constants'

export const login = (payload) => ({
    type: types.PUSH_LOGIN,
    payload
})

export const signup = (payload) => ({
    type: types.PUSH_SIGNUP,
    payload
})

export const retryConnection = () => ({
    type: types.RETRY_CONNECT
})