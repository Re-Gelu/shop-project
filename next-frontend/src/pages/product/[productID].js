import { useState, useEffect } from "react";
import { useRouter } from 'next/router'
import axios from '@/api.js';

const ProductPage = ({product}) => {
    const router = useRouter();

   	if (router.isFallback) {
		return <div>Загрузка...</div>
	}

    return (
        <div>{product.name}</div>
    );
};

export async function getServerSideProps(context) {
	const productResponse = await axios.get(`products/${context.query.productID}`);
	const product = productResponse.data;
	return {
		props: {
			product
		}
	}
};

/* export async function getStaticPaths() {
	return {
		paths: [
			{ params: {productID} }
		],
		fallback: false
	}
} */

export default ProductPage;