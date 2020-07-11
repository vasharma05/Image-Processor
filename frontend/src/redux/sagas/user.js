import {takeEvery, select, call, put} from 'redux-saga/effects'
import * as api from '../../network'
import checkAPIfailure from '../../network/utils'
import * as types from '../constants'

const getToken = state => state.auth.signinData
function* uploadImage(request){
    let token = yield select(getToken)
    const payload = request.payload
    try{
        const response = yield call(api.uploadImage, payload, token)
        const checkResponse = checkAPIfailure(response)
        if(checkResponse.detail === 'success'){
            yield put({type: types.SET_IMAGE_URL, image: checkResponse.response})
        }
    }catch(error){
        console.log(error)
        yield put({type: 'NETWORK_ERROR'})

    }
}

function* fetchUserImages(request){
    const token = yield select(getToken)
    try{
        const response = yield call(api.fetchUserImages, token)
        const checkResponse = checkAPIfailure(response)
        if(checkResponse.detail === 'success'){
            yield put({type: 'SET_USER_IMAGES', images: checkResponse.response})
        }
    }catch(error){
        console.log(error)
        yield put({type: 'NETWORK_ERROR'})

    }
}

function* getFilterImage(request){
    const token = yield select(getToken)
    const {filter, id} = request
    try{
        const response = yield call(api.getFilterImage, filter, id, token)
        const checkResponse = checkAPIfailure(response)
        console.log(checkResponse)
        if(checkResponse.detail === 'success'){
            yield put({type: 'SET_FILTER_IMAGE',filter: filter, image: JSON.parse(checkResponse[filter])})
        }
    }catch(error){
        console.log(error)
        yield put({type: 'NETWORK_ERROR'})

    }
}

function* userSaga(){
    return [
        yield takeEvery(types.UPLOAD_IMAGE, uploadImage),
        yield takeEvery('FETCH_USER_IMAGES', fetchUserImages),
        yield takeEvery('GET_FILTER_IMAGE', getFilterImage)
    ]
}

export default userSaga