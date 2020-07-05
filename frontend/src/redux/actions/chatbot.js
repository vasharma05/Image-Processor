import * as types from '../constants'

export const getChatbotDetails = () => ({
    type: types.GET_CHATBOT_DETAILS
})

export const sendChatbotDetails = (payload) => ({
    type: types.SEND_CHATBOT_MESSAGE,
    payload
})

export const sendConsumerEmail = (payload) => ({
    type: types.SEND_CONSUMER_EMAIL,
    payload
})