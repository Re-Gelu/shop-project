import axios from '@/api.js';
import ShopPage from "@/components/ShopPage";
import MainLayout2 from '@/components/MainLayout2.js';

const ProductPage2 = (props) => {
    const {
		categories,
		subcategories,
        products,
        total_pages,
        current_page_number
    } = {...props};

    return (
        <MainLayout2 {...{categories, subcategories}}>
            <ShopPage {...props} />
        </MainLayout2>
    );
};

export async function getStaticPaths() {
    const categoriesResponse = await axios.get('categories');
    const paths = [];

    for (const category of categoriesResponse.data) {
        const pagesAmountResponse = await axios.get(`products/?page=1&subcategory__category=${category.id}`);
        for (const page of Array.from({length: pagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
            paths.push({
                params: {
                    category: category.id.toString(),
                    subcategory: page.toString(),
                },
            });
        };
    };

    return {
        paths: paths,
        fallback: false,
    };
};


export async function getStaticProps({ params }) {
	const categoriesResponse = await axios.get('categories');
	const subcategoriesResponse = await axios.get('subcategories');
    const productsResponse = await axios.get(`products/?page=${params.subcategory}&subcategory__category=${params.category}`);
    
	return {
		props: {
			categories: categoriesResponse.data,
			subcategories: subcategoriesResponse.data,
            products: productsResponse.data.results,
            total_pages: productsResponse.data.total_pages,
            current_page_number: productsResponse.data.current_page_number
		}
	};
};


export default ProductPage2;