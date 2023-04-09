import MainLayout2 from '@/components/MainLayout2.js';
import TopRow from "@/components/TopRow.js";
import ProductPageCard from '@/components/ProductPageCard.js';
import axios from '@/api.js';
import {fetchAllData} from '@/api.js';
import { INTERNAL_API_SERVER_URL } from '@/config.js';


const ProductPage = (props) => {
	const {
		categories,
		subcategories,
		product
	} = {...props};

    return (
		<MainLayout2 {...{categories, subcategories}}>
			<TopRow {...props}/>
			<ProductPageCard {...{product}}/>
		</MainLayout2>
    );
};

export async function getStaticPaths() {
	const data = await fetchAllData(`${INTERNAL_API_SERVER_URL}products/?page=1`);
	return {
		paths: data.map((product) => ({
			params: { productID: product.id.toString() }
		})),
		fallback: true
	};
};

export async function getStaticProps({ params }) {
    const productResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/${params.productID}`);
	const categoriesResponse = await axios.get(`${INTERNAL_API_SERVER_URL}categories`);
	const subcategoriesResponse = await axios.get(`${INTERNAL_API_SERVER_URL}subcategories`);
	const categories = categoriesResponse.data;
	const subcategories = subcategoriesResponse.data;
	const product = productResponse.data;
	return {
		props: {
			categories,
			subcategories,
			product
		}
	};
};

export default ProductPage;