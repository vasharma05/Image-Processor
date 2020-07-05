import { combineReducers } from 'redux'
import authReducers from './auth'
import chatbotReducer from './chatbot'

const rootReducer = combineReducers({
    auth: authReducers,
    chatbot: chatbotReducer
})

export default rootReducer