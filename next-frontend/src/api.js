import axios from 'axios';
import {API_SERVER_URL} from '@/config.js';

export default axios.create({
    baseURL: API_SERVER_URL,
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFToken"
});