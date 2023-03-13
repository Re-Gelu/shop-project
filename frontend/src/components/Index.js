import { useState, useEffect } from "react";
import { MEDIA_SERVER_URL } from "../config.js";
import axios from '../api.js';
import Base from './Base.js'

const Index = (props) => {

    const [IndexPageData, setIndexPageData] = useState([]);

    useEffect(() => {
        axios.get('index_page')
        .then(response => {setIndexPageData(response.data); console.log(response.data);})
        .catch(error => console.log(error));
    }, []);


    return (<div>Index</div>)
};

export default Index;