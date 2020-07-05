import { all } from 'redux-saga/effects'
import authSaga from './auth'
import chatSaga from './chatbot'

function* rootSaga(){
    yield all([authSaga(), chatSaga()])
}

export default rootSaga