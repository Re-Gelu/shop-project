import { useRouter } from "next/router";
import axios from '@/api.js';
import ShopPage from "@/components/ShopPage";
import MainLayout2 from '@/components/MainLayout2.js';

const ProductPage = (props) => {
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
            const pagesAmountResponse = await axios.get(`products/?page=1&subcategory=${subcategory.id}`);
            for (const page of Array.from({length: pagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
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

    for (const category of categoriesResponse.data) {
        const pagesAmountResponse = await axios.get(`products/?page=1&subcategory__category=${category.id}`);
        for (const page of Array.from({length: pagesAmountResponse.data.total_pages}, (_, i) => i + 1)) {
            paths.push({
                params: {
                    slug: [
                        category.id.toString(),
                        page.toString(),
                    ]
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
    const slug = params.slug;
	const categoriesResponse = await axios.get('categories');
	const subcategoriesResponse = await axios.get('subcategories');
    let productsResponse = [];

    if (slug.length === 3) {
        productsResponse = await axios.get(`products/?page=${slug[2]}&subcategory=${slug[1]}`);
    } else if (slug.length === 2) {
        productsResponse = await axios.get(`products/?page=${slug[1]}&subcategory__category=${slug[0]}`);
    } else if (slug.length === 1) {
        productsResponse = await axios.get(`products/?page=${slug[0]}`);
    }

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


export default ProductPage;