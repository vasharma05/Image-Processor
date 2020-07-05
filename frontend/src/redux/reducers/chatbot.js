import * as types from '../constants'

let initState = {
    message: null,
    chatbotDetails:null,
    consumer: null
}

const updateObject = (state, newState) => ({
    ...state,
    ...newState
})

const setChatbotDetails = (state, action) =>
    updateObject(state, {
        message: null,
        chatbotDetails: action.payload
    })

const setChatbotMessage = (state,action) => 
    updateObject(state, {
        message: action.message,
        chatbotDetails: null
    })

const setConsumerEmail = (state, action) => 
    updateObject(state, {
        consumer: action.consumer
    })

function chatbotReducer(state=initState, action){
    switch(action.type){
        case types.GET_CHATBOT_DETAILS:
            return updateObject(state, {
                chatbotDetails:null
            })
        case types.SET_CHATBOT_DETAILS:
            return setChatbotDetails(state, action)
        case types.SET_CHATBOT_MESSAGE:
            return setChatbotMessage(state, action)
        case types.SET_CONSUMER:
            return setConsumerEmail(state, action)
        default:
            return state
    }
}

export default chatbotReducer