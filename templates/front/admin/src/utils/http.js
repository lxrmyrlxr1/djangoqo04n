import axios from 'axios'
import router from '@/router/router-static'
import storage from '@/utils/storage'

const http = axios.create({
    timeout: 1000 * 86400,
    withCredentials: true,
    baseURL: '/djangoqo04n',
    headers: {
        'Content-Type': 'application/json; charset=utf-8'
    }
})

http.interceptors.request.use(config => {
    config.headers['Token'] = storage.get('Token') // token
    return config
}, error => {
    return Promise.reject(error)
})

http.interceptors.response.use(response => {
    if (response.data && response.data.code === 401) { // 401, token
        router.push({ name: 'login' })
    }
    return response
}, error => {
    return Promise.reject(error)
})
export default http
