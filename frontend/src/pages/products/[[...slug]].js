import axios from '@/api.js';
import ShopPage from "@/components/ShopPage";
import MainLayout2 from '@/components/MainLayout2.js';
import { INTERNAL_API_SERVER_URL } from '@/config.js';


const ProductPage = (props) => {
    const {
		categories,
		subcategories
    } = {...props};

    return (
        <MainLayout2 {...{categories, subcategories}}>
            <ShopPage {...props} />
        </MainLayout2>
    );
};

export async function getStaticPaths() {
    const categoriesResponse = await axios.get(`${INTERNAL_API_SERVER_URL}categories`);
    const subcategoriesResponse = await axios.get(`${INTERNAL_API_SERVER_URL}subcategories`);
    const paths = [];

    for (const category of categoriesResponse.data) {
        const categoriesPagesAmountResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=1&subcategory__category=${category.id}`);
        for (const page of Array.from({length: categoriesPagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
            paths.push({
                params: {
                    slug: [
                        category.id.toString(),
                        page.toString(),
                    ]
                },
            });
        };
        for (const subcategory of subcategoriesResponse.data.filter(subcategory => subcategory.category === category.id)) {
            const subcategoriesPagesAmountResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=1&subcategory=${subcategory.id}`);
            for (const page of Array.from({length: subcategoriesPagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
                paths.push({
                    params: {
                        slug: [
                            category.id.toString(),
                            subcategory.id.toString(),
                            page.toString(),
                        ]
                    },
                });
            };
        };
    };

    const productsPagesAmountResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=1`);
    for (const page of Array.from({length: productsPagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
        paths.push({
            params: {
                slug: [
                    page.toString(),
                ]
            },
        });
    };

    return {
        paths: paths,
        fallback: false,
    };
};


export async function getStaticProps({ params }) {
    const slug = params.slug;
	const categoriesResponse = await axios.get(`${INTERNAL_API_SERVER_URL}categories`);
	const subcategoriesResponse = await axios.get(`${INTERNAL_API_SERVER_URL}subcategories`);
    let productsResponse = [];
    let category = null;
	let subcategory = null;
	let page = null;

    if (slug.length >= 3) {
        productsResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=${slug[2]}&subcategory=${slug[1]}`);
        category = slug[0]
        subcategory = slug[1];
		page = slug[2];
    } else if (slug.length === 2) {
        productsResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=${slug[1]}&subcategory__category=${slug[0]}`);
        category = slug[0];
		page = slug[1];
    } else if (slug.length === 1) {
        productsResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=${slug[0]}`);
        page = slug[0];
    } else {
        productsResponse = await axios.get(`${INTERNAL_API_SERVER_URL}products/?page=1`);
        page = '1';
    }

	return {
		props: {
			categories: categoriesResponse.data,
			subcategories: subcategoriesResponse.data,
            products: productsResponse.data.results,
            total_pages: productsResponse.data.total_pages,
            category: category,
            subcategory: subcategory,
            page: productsResponse.data.current_page_number,
		}
	};
};


export default ProductPage;