import axios from 'axios'
const baseURL = 'http://127.0.0.1:8000/'

class Api {
    static get(route, params){
        return this.request(route, params, 'get')
    }
    static post(route, params){
        return this.request(route, params, 'post')
    }
    static getWithToken(route, token, params){
        return this.requestWithToken(route, params, 'GET', token)
    }
    static postWithToken(route, token, params){
        return this.requestWithToken(route, params, 'POST', token)
    }
    static requestWithToken(route, params, verb, token){
        const host = baseURL;
        const url = `${host}${route}`;
        const options = { method: verb, data: params };
        options.headers = {
            'Authorization': 'Token ' + token,
            // 'content-type': 'multipart/form-data'
        }
        options.crossOrigin = true
        console.log(`Options*******************${JSON.stringify(options)}`);
        console.log(`URL*********************${JSON.stringify(url)}`);
        console.log(url, options)
        return axios(url, options);
    }
    static request(route, params, verb) {
        const host = baseURL;
        const url = `${host}${route}`;
        const options = { method: verb, data: params };
        options.headers = {}
        options.crossOrigin = true
        console.log(`Options*******************${JSON.stringify(options)}`);
        console.log(`URL*********************${JSON.stringify(url)}`);
        console.log(url, options)
        return axios(url, options);
      }
}

export default Api