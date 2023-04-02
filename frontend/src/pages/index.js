import { Inter } from 'next/font/google';
import React from "react";
import MainLayout2 from '@/components/MainLayout2.js';
import Index from '@/components/Index.js';
import axios from '@/api.js';

const inter = Inter({ subsets: ['latin'] })

const IndexPage = (props) => {
	const {
		categories,
		subcategories,
		index
  	} = {...props};

	return (
		<MainLayout2 {...{categories, subcategories}}>
			<Index {...{index}} />
		</MainLayout2>
	)
};

export async function getStaticProps() {
	const categoriesResponse = await axios.get('categories');
	const subcategoriesResponse = await axios.get('subcategories');
	const indexResponse = await axios.get('index_page');
	const categories = categoriesResponse.data;
	const subcategories = subcategoriesResponse.data;
	const index = indexResponse.data;
	return {
		props: {
			categories,
			subcategories,
			index
		}
	}
};

export default IndexPage;