import { combineReducers } from 'redux'
import authReducers from './auth'
import userReducer from './user'

const rootReducer = combineReducers({
    auth: authReducers,
    user: userReducer
})

export default rootReducer