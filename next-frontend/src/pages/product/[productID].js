import { useState, useEffect } from "react";
import { useRouter } from 'next/router'
import axios from '@/api.js';
import {fetchAllData} from '@/api.js';

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
	const data = await fetchAllData(`products/?page=1`);
	const paths = data.map((product) => ({
		params: {
			productID: product.id.toString(),
			product: product
		}
	}));
	return {
		paths: paths,
		fallback: false
	};
};

export async function getStaticProps({ params }) {
	console.log(params.product);
	const product = params.product;
	const productID = params.productID;
	return {
		props: {
			product,
			productID
		},
		revalidate: 3
	}
};

export default ProductPage;