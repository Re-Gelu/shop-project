import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import axios from '../api.js';

const Base = (props) => {

    const [categories, setCategories] = useState([]);
    const [subcategories, setSubcategories] = useState([]);

    useEffect(() => {
        axios.get('categories')
        .then(response => setCategories(response.data))
        .catch(error => console.log(error));

        axios.get('subcategories')
        .then(response => setSubcategories(response.data))
        .catch(error => console.log(error));
    }, []);

    return (
        <div className="row">
        <div className="col-xl-3 col-12 pt-3">
            <aside className="sidebar">

                <nav className="ms-1 mb-1 card">
                    <div className="card-header">
                        <p className="text-center lead sidebar-menu-header my-2"><i className="bi bi-list"></i> Категории:</p>
                    </div>
                    <ul className="card-body list-unstyled">
                        {categories.map((category, key) =>
                            <span key={key}>
                                <li className="my-3 px-0 text-left container"><a href={"products/" + category.name}>{category.name}<i className="bi bi-caret-right pe-1 float-end "></i></a></li>
                                
                                <div uk-dropdown="pos: right-top; animation: uk-animation-slide-left-medium; duration: 300;">
                                    <div>
                                        <ul className="uk-nav uk-dropdown-nav p-0">  
                                            <hr className="text-black-50"/>
                                            {subcategories.map((subcategory, key) =>
                                                subcategory.category == category.id &&
                                                    <span key={key}>
                                                        <li ><a href={"products/" + category.name + '/' + subcategory.name} className="a-important">{subcategory.name}</a></li>
                                                        <hr className="text-black-50"></hr>
                                                    </span>
                                            )}
                                        </ul>
                                    </div>
                                </div>

                                {!(key == categories.length - 1) &&
                                    <hr className="text-black-50"/>
                                }
                            </span>
                        )} 
                    </ul>
                </nav>

                <section className="ms-1 mb-1 mt-3 card d-none d-md-block">
                    <div className="card-header">
                        <p className="text-center lead sidebar-menu-header my-2"><i className="bi bi-hand-thumbs-up small"></i> Возможно вам понравится:</p>
                    </div>

                        <div className="col-12">
                            {/* {% include "product_card.html" with product=random_product %} */}
                        </div>
                </section>
            </aside>
        </div>

        <div className="col-xl-9 col-12 pt-3">  
            <Outlet />
        </div>
        </div>
    );
};

export default Base;