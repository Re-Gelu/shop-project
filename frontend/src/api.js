import axios from 'axios';
import {API_SERVER_URL} from '@/config.js';

const custom_axios = axios.create({
    baseURL: API_SERVER_URL,
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFToken"
});

async function fetchData(url) {
    const response = await custom_axios.get(url);
    return response.data;
}

export async function fetchAllData(url) {
    let results = [];
    let response = await fetchData(url);
    results = results.concat(response.results);
    
    while (response.next !== null) {
        response = await fetchData(response.next);
        results = results.concat(response.results);
    }
    return results;
}

export default custom_axios;