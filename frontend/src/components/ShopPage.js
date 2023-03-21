import { useState, useEffect } from "react";
/* import { useParams } from 'react-router-dom'; */
import axios from '../api.js';
import ProductCard from "./ProductCard.js";

const ProductPage = (props) => {
    const [products, setProducts] = useState([]);
    const {category, subcategory} = useParams();
    const page = 1

    useEffect(() => {
        axios.get(`products/?page=${page}`)
        .then(response => {
            setProducts(response.data.results);
            console.log(response.data);
        })
        .catch(error => console.log(error));
    }, []);

    return (
        <div className="col-xl-9 col-12 pt-3">  
            <div className="row mt-1 g-2">
                { (products.length !== 0) ?
                    products.map((product) => (
                        <div className="col-xl-3" key={product.id}>
                            <ProductCard product={product} />
                        </div>
                    ))
                :
                    /* <!-- No products in category --> */
                    <div className="container col-xl-5 col-12 p-5">
                        <div className="row g-3 text-center">
                            <p className="h2">Товаров пока нет!</p>
                            <hr />
                            <p>Возможно когда нибудь я их даже добавлю (но это не точно)</p>
                        </div>
                    </div>
                }
            </div>
        </div>
    );
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