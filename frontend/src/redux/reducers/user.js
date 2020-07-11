import * as types from '../constants'

let initState = {
    imageList: null,
    imageId: null,
    image: null,
    centroid : null,
    gradient : null,
    negative : null,
    grayscale : null,
    segmentation : null,
    histogram : null,
    average : null,
    gaussian : null,
    median : null,
    sobel : null,
}

const updateObject = (state, newState) => ({
    ...state,
    ...newState
})

const setImageList = (state, action) => 
    updateObject(state, {
        imageList: action.images
    })

const setFilterImage = (state, action) => {
    console.log(action.image)
    const {filter} = action
    return updateObject(state, {
        [filter] : action.image
    })
}

function userReducer(state=initState, action){
    switch(action.type){
        case types.SET_IMAGE_URL:
            return updateObject(state, {
                image: action.image.image,
                imageId: action.image.id,
                imageList: [...state.imageList,action.image]
            })
        case 'SET_USER_IMAGES':
            return setImageList(state, action)
        case 'SET_FILTER_IMAGE':
            return setFilterImage(state, action)
        case types.RESET_IMAGE:
            return updateObject(state, {
                imageId: null,
                image: null,
                centroid : null,
                gradient : null,
                negative : null,
                grayscale : null,
                segmentation : null,
                histogram : null,
                average : null,
                gaussian : null,
                median : null,
                sobel : null,
            })
        default:
            return state
    }
}

export default userReducer