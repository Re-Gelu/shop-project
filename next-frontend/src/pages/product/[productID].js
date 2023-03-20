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

export async function getStaticPaths() {
	const productResponse = await axios.get(`products/`);
	const productAmount = productResponse.data.count;
	const paths = [...Array(productAmount).keys()].map((product) => ({
		params: {productID: product.toString()}
	}));
	return {
		paths: paths,
		fallback: false
	}
}

export async function getStaticProps({ params }) {
    const productResponse = await axios.get(`products/${params.productID}`);
	const product = productResponse.data;
	return {
		props: {
			product
		}
	}
}

export default ProductPage;