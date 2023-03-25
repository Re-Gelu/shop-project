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
    const subcategoriesResponse = await axios.get('subcategories');
    const paths = [];

    for (const category of categoriesResponse.data) {
        for (const subcategory of subcategoriesResponse.data.filter(subcategory => subcategory.category === category.id)) {
            const pagesAmountResponse = await axios.get(`products/?page=1&subcategory=${subcategory.id}`)
            for (const page of Array.from({length: pagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
                paths.push({
                    params: {
                        category: category.id.toString(),
                        subcategory: subcategory.id.toString(),
                        page: page.toString(),
                    },
                });
            };
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
    const productsResponse = await axios.get(`products/?page=${params.page}&subcategory=${params.subcategory}`);
    
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