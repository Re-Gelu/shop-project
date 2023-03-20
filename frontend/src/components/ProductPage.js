import { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import axios from '../api.js';

const ProductPage = (props) => {
    const [product, setProduct] = useState({});
    const {productID} = useParams();

    useEffect(() => {
        if (productID) {
            axios.get(`products/${productID}`)
            .then(response => {
                setProduct(response.data);
                console.log(response.data);
            })
            .catch(error => console.log(error));
        };
    }, [productID]);

    return (
        <div>{product.name}</div>
    );
};

export default ProductPage;