import Api from './apiConfig'

export const login = (payload) => Api.post('accounts/api/login/', payload)
export const signup = (payload) => Api.post('accounts/api/signup/', payload)
export const uploadImage = (payload, token) => Api.postWithToken('accounts/api/upload/', payload, token)
export const fetchUserImages = (token) => Api.getWithToken('accounts/api/images/', null, token)
export const getFilterImage = (filter, id, token) => Api.postWithToken(`accounts/api/${filter}/`, id, token)