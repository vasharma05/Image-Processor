import Api from './apiConfig'

export const login = (payload) => Api.post('accounts/api/login/', payload)
export const signup = (payload) => Api.post('accounts/api/signup/', payload)
export const getChatbotDetails = (token) => Api.getWithToken('chatbot/api/', token)
export const sendChatbotDetails = (payload, token) => Api.postWithToken('chatbot/api/', token, payload)
export const sendConsumerEmail = (payload) => Api.post('chatbot/consumeremail/', payload)