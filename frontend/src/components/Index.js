import ProductCard from "@/components/ProductCard.js";
import React from "react";
import Link from 'next/link';

const Index = ({index}) => {
	return (
		<>
			{index && index.map(category =>
                <section className="row mt-3 g-0" key={category.id}>

                    <div className="uk-card border p-3">
                        
                        <div>
                            <Link href={`/products/${category.id}/1`} className="row my-2 ms-2 lead text-colored d-inline-block"><i className="bi bi-caret-right"></i>{category.name}</Link>
                            <hr className="border-top-colored"/>

                            <div className="row uk-position-relative uk-visible-toggle px-3 uk-slider uk-slider-container" 
								tabIndex="-1" uk-slider="sets: true, finite: true, draggable: true"
								role="region" ariaroledescription="carousel">
                                
                                <ul aria-live="polite" role="presentation" className="uk-slider-items uk-child-width-1-1 uk-child-width-1-2@s uk-child-width-1-3@m uk-child-width-1-4@l" style={{"maxHeight    ": 100 + "%"}}>

                                    <li id="scroller-item" className="card me-4 overflow-auto" tabIndex="0">
										<div className="card-header">
											<div className="lead text-colored">Подкатегории: </div>
										</div>

										<div className="card-body">
											{index && category.subcategories.map((subcategory, key) => {
													if (subcategory.category === category.id) {
														return (
															<React.Fragment key={subcategory.id}>
																<p className="my-3">
																	<Link href={`/products/${category.id}/${subcategory.id}/1`} className="uk-button-text my-2 a-important">
																		{subcategory.name}
																	</Link>
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
                                                <Link className="card-body lead fs-3 text-colored my-5 py-5 text-center" href={`/products/${category.id}`}>
                                                    Больше товаров...
                                                </Link>
                                            </div>
                                        </li>
                                    )}

                                </ul>
                            </div>
                            
                        </div>
                    </div>

                </section>
            )}
		</>
	);
};

export default Index;