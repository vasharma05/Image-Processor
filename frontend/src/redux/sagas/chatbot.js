import {takeEvery, select, call, put} from 'redux-saga/effects'
import * as api from '../../network'
import checkAPIfailure from '../../network/utils'
import * as types from '../constants'

const getToken = state => state.auth.signinData

function* getChatbotDetails(request){
    let token = yield select(getToken)
    try{
        const response = yield call(api.getChatbotDetails, token)
        const checkResponse = checkAPIfailure(response)
        if(checkResponse.detail === 'success'){
            yield put({type: 'SET_CHATBOT_DETAILS', payload: checkResponse.chatbot_details})
        }else if(checkResponse.detail === 'No chatbot details found'){
            yield put({type: 'SET_CHATBOT_MESSAGE', message: checkResponse.detail})
        }else{
            console.log(checkResponse)
        }
    }catch(error){
        console.log(error)
        yield put({type: 'NETWORK_ERROR'})

    }
}

function* sendChatbotDetails(request){
    let token = yield select(getToken)
    console.log(request)
    try{
        const response = yield call(api.sendChatbotDetails, request.payload, token)
        const checkResponse = checkAPIfailure(response)
        if(checkResponse.detail === 'success'){
            yield put({type: 'SET_CHATBOT_MESSAGE', message: checkResponse.detail})
        }else{
            yield put({type: 'SET_CHATBOT_MESSAGE', message: 'failed'})
        }
    }catch(error){
        console.error(error)
        yield put({type: 'NETWORK_ERROR'})
    }
}

function* sendConsumerEmail(request){
    let payload = request.payload
    console.log(request)
    try{
        const response = yield call(api.sendConsumerEmail, payload)
        const checkResponse = checkAPIfailure(response)
        if(checkResponse.message === 'success'){
            yield put({type:'SET_CONSUMER',  consumer: checkResponse.consumer})
        }
    }catch(error){
        console.error(error)
        yield put({type: 'NETWORK_ERROR'})
    }
}

function* chatSaga(){
    return [
        yield takeEvery('GET_CHATBOT_DETAILS', getChatbotDetails),
        yield takeEvery(types.SEND_CHATBOT_MESSAGE, sendChatbotDetails),
        yield takeEvery(types.SEND_CONSUMER_EMAIL, sendConsumerEmail)
    ]
}

export default chatSaga