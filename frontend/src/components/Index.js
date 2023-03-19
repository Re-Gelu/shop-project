import { useState, useEffect } from "react";
import ProductCard from "./ProductCard.js";
import React from "react"
import axios from '../api.js';

const Index = (props) => {

    const [IndexPageData, setIndexPageData] = useState([]);

    useEffect(() => {
        axios.get('index_page')
        .then(response => setIndexPageData(response.data))
        .catch(error => console.log(error));
    }, []);

    return (
        <div className="col-xl-9 col-12 pt-3">  
            {IndexPageData.map(category =>
                <section className="row mt-3 g-0" key={category.id}>

                    <div className="uk-card border p-3">
                        
                        <div>
                            <a href={`/products/${category.name}`} className="row my-2 ms-2 lead text-colored d-inline-block"><i className="bi bi-caret-right"></i>{category.name}</a>
                            <hr className="border-top-colored"/>

                            <div className="row uk-position-relative uk-visible-toggle px-3" tabIndex="-1" uk-slider="sets: true, finite: true, draggable: true">
                                
                                <ul className="uk-slider-items uk-child-width-1-1 uk-child-width-1-2@s uk-child-width-1-3@m uk-child-width-1-4@l" style={{"maxHeight    ": 100 + "%"}}>

                                    <li id="scroller-item" className="card me-4 overflow-auto" tabIndex="0">
                                            <div className="card-header">
                                                <a href="#" className="lead text-colored">Подкатегории: </a>
                                            </div>

                                            <div className="card-body">
                                               {category.subcategories.map((subcategory, key) => {
                                                    if (subcategory.category === category.id) {
                                                        return (
                                                            <React.Fragment key={subcategory.id}>
                                                                <p className="my-3">
                                                                    <a href={`/products/${category.name}/${subcategory.name}`} className="uk-button-text my-2 a-important">
                                                                        {subcategory.name}
                                                                    </a>
                                                                </p>
                                                                {key !== category.subcategories.length - 1 && 
                                                                    <hr className="text-black-50" />
                                                                }
                                                            </React.Fragment>
                                                        );
                                                    }
                                                    return null;
                                                })}
                                            </div>
                                    </li>

                                    {category.products.map((product) => (
                                        <li id="scroller-item" className="me-3" key={product.id}>
                                            <ProductCard product={product} cardAnimationClass="uk-transition-slide-left-small" />
                                        </li>
                                    ))}

                                    {category.products.length > 0 && (
                                        <li className="uk-transition-toggle me-3">
                                            <div className="h-100 card uk-card-hover uk-transition-opaque uk-transition-slide-left-small py-5">
                                                <a className="card-body lead fs-3 text-colored my-5 py-5 text-center" href={`/products/${category.name}`}>
                                                    Больше товаров...
                                                </a>
                                            </div>
                                        </li>
                                    )}

                                </ul>
                            </div>
                            
                        </div>
                    </div>

                </section>
            )}
        </div>
    )
};

export default Index;