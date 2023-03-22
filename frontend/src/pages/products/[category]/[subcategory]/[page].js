import { useState, useEffect } from "react";
import axios from '@/api.js';
import { fetchAllData } from '@/api.js';
import ShopPage from "@/components/ShopPage";
import MainLayout2 from '@/components/MainLayout2.js';

const ProductPage = (props) => {
    const {
		categories,
		subcategories,
        products
    } = {...props};

    return (
        <MainLayout2 {...{categories, subcategories}}>
            <ShopPage {...{products}} />
        </MainLayout2>
    );
};

export async function getStaticPaths() {
    const data = await fetchAllData(`products/?page=1`);
	return {
		paths: data.map((product) => ({
			params: { 
                category: product.category.toString(),
                subcategory: product.category.toString(),
                page: "1"
            }
		})),
		fallback: true
	};
};

export async function getStaticProps({ params }) {
	const categoriesResponse = await axios.get('categories');
	const subcategoriesResponse = await axios.get('subcategories');
	const categories = categoriesResponse.data;
	const subcategories = subcategoriesResponse.data;
    const productsResponse = await axios.get(`products/?page=${params.page}`);
    const products = productsResponse.data;
	return {
		props: {
			categories,
			subcategories,
            products,
		}
	};
};


export default ProductPage;

/* <!-- Pagination --> */
            /* <nav>
                <ul class="pagination justify-content-center flex-wrap mt-3 mb-4 fs-4">

                    <!-- previous_page -->
                    {% if products.has_previous %}
                        <li class="page-item"><a class="page-link text-colored" href="?page={{products.previous_page_number}}">&laquo;</a></li>
                    {% else %}
                        <li class="disabled page-item"><span class="page-link">&laquo;</span></li>
                    {% endif %}

                    <!-- pagination -->
                    {% for page in page_range %}
                        {% if products.number == page %}
                            <li class="active page-item"><span class="page-link background-colored border-colored">{{page}}</span></li>
                        {% else %}
                            {% if page == products.paginator.ELLIPSIS %}
                                <li class="page-item"><span class="page-link text-colored">{{page}}</span></li>
                            {% else %}
                                
                            <!--  <li class="page-item"><a class="page-link" href="{% url 'products' %}{{request.get_full_path|cut:request.path}}&page={{page}}">{{page}}</a></li> -->
                            <li class="page-item"><a class="page-link text-colored" href="?page={{page}}">{{page}}</a></li>
                            {% endif %}
                        {% endif %}
                    {% endfor %}

                    <!-- next_page -->
                    {% if products.has_next %}
                        <!-- <li class="page-item"><a class="page-link" href="{% url 'products' %}{{request.get_full_path|cut:request.path}}&page={{products.next_page_number}}">&raquo;</a></li> -->
                        <li class="page-item"><a class="page-link text-colored" href="?page={{products.next_page_number}}}">&raquo;</a></li>
                    {% else %}
                        <li class="disabled page-item"><span class="page-link">&raquo;</span></li>
                    {% endif %}
                </ul>
            </nav> */