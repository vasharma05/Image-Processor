import * as types from '../constants'

export const uploadImage = (payload) => ({
    type: types.UPLOAD_IMAGE,
    payload
})
export const resetImage = (payload) => ({
    type: types.RESET_IMAGE
})

export const fetchUserImages = () => ({
    type: 'FETCH_USER_IMAGES'
})

export const getFilterImage = (filter, id) => ({
    type: "GET_FILTER_IMAGE",
    filter,
    id
})