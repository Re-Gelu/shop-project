import { useContext } from "react";
import { MEDIA_SERVER_URL } from "@/config.js";
import { ApiContext } from '@/components/ApiContext.js';
import Link from 'next/link';

const CartOffcanvas = (props) => {
	const { 
		cart, 
		cartTotalPrice,
		cartTotalPromoPrice, 
		cartEventHandler
	} = useContext(ApiContext);

	return (
		/* <!-- Offcanvas --> */
        <aside id="shopping-cart-offcanvas" className="offcanvas offcanvas-end" tabIndex="-1" aria-labelledby="shopping-cart-offcanvas-label">
            
            {/* <!-- Offcanvas header--> */}
            <div className="offcanvas-header my-1">
                <p className="offcanvas-title h4 header-element badge uk-button-text" id="shopping-cart-offcanvas-label">Корзина  <i className="bi bi-cart2"></i></p>
                <button type="button" className="btn-close btn-lg border-colored" data-bs-dismiss="offcanvas" aria-label="Закрыть"></button>
            </div>

            {/* <!-- Decoration --> */}
            <hr className="border-top-colored" />

            {/* <!-- Offcanvas body--> */}
            <div id="cart-offcanvas-body" className="offcanvas-body">
				<div>
					{(!Object.keys(cart).length) ?
						<div className="lead fs-3 text-colored my-5 py-5 text-center">
							Корзина пуста
						</div>
					:
						<>
						<div className="p-2">
							{cart.map((product, key) => 
								<div className="uk-transition-toggle" key={key}>
									<div className="uk-card-hover uk-transition-scale-up uk-transition-opaque d-flex border p-3" aria-hidden="true">
										
										<img src={MEDIA_SERVER_URL + product.image} alt={"Product " + product.id} 
										className="flex-shrink-0 me-3 my-auto rounded uk-transition-scale-up uk-transition-opaque" width="60" height="60" />
										<div className="row g-3">
											<div className="col-12">
												<Link href={`product/${product.id}/`} className="lead uk-button-text">{product.name}</Link>
												<button id="cart-offcanvas-remove-btn" product-id={product.id} className="btn-close btn-sm float-end" aria-label="Delete product"
												onClick={(e) => cartEventHandler(e, {"id": product.id, "action": false,"amount": 100})}></button>
											</div><br />

											<div className="row col-12 mx-0 mt-2 px-2">
												<span className="col-4 p-0">Кол-во: </span>

												<div id="cart-offcanvas-remove-one-btn" product-id={product.id} className="col-1 p-0" 
												onClick={(e) => cartEventHandler(e, {"id": product.id, "action": false,"amount": 1})}>
													<button className="col-4 border-0 p-0 bg-transparent"><i className="bi bi-dash-lg"></i></button>
												</div>

												<span className="col-1 p-0">{product.product_amount}</span> 
												
												<div id="cart-offcanvas-add-one-btn" product-id={product.id} className="col-1 p-0"
												onClick={(e) => cartEventHandler(e, {"id": product.id, "action": true, "amount": 1})}>
													<button className="col-4 border-0 p-0 bg-transparent"><i className="bi bi-plus-lg"></i></button>
												</div>
											</div><br />

											{
												product.total_promo_price ?
													<div className="col-12">
														<span className="text-decoration-line-through me-2">{product.total_price} RUB</span>
														<span className="text-danger">{product.total_promo_price} RUB</span>
													</div>
												:	
													<div className="col-12">
														<span>{product.total_price} RUB</span>
													</div>
											}
										</div>
									</div>
								</div>
							)}
						</div>

						<hr className="border-top-colored"></hr>

						<div className="h5">
							Итого:  
							{
								(cartTotalPromoPrice < cartTotalPrice) ? 
									<span>
										<span className="text-decoration-line-through h4 mx-2">{cartTotalPrice} RUB</span>
										<span className="text-danger h4">{cartTotalPromoPrice} RUB</span>
									</span>
								:
									<span className="h4">{cartTotalPrice} RUB</span>
							}
						</div>

						<div className="d-grid gap-2">
							<a type="button" className="btn btn-lg uk-button-text border-colored">Перейти к оформлению заказа</a>
						</div>
						</>
					}
				</div>
			</div>

            {/* <!-- Decoration --> */}
            <hr className="border-top-colored" />
        </aside>
	);
};

export default CartOffcanvas;