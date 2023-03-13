import { useState, useEffect } from "react";
import { MEDIA_SERVER_URL } from "../config.js";
import axios from '../api.js';

const CartOffcanvas = (props) => {
	const [cart, setCart] = useState({});
	const [cartTotalPrice, setCartTotalPrice] = useState(0);
	const [cartTotalPromoPrice, setCartTotalPromoPrice] = useState(0);

	useEffect(() => {
		axios.get('cart')
		.then(response => {
			setCart(response.data.cart);
			setCartTotalPrice(response.data.cart_total_price);
			setCartTotalPromoPrice(response.data.cart_total_promo_price);
		})
		.catch(error => console.log(error));
	}, [setCart]);

	const cartEventHandler = (e, data) => {
		axios.post('cart/', data)
		.then(response => {
			setCart(response.data.cart);
			setCartTotalPrice(response.data.cart_total_price);
			setCartTotalPromoPrice(response.data.cart_total_promo_price);
		})
		.catch(error => console.log(error))
		/* if (element.getAttribute("id") === "cart-add-one-btn") {
			cart_animation(element);
		} */
	};

	if (!Object.keys(cart).length) {
		return (
			<button className="lead fs-3 text-colored my-5 py-5 text-center" 
			onClick={ () => {
				axios.post('cart/', {
					id: 106,
					amount: 1,
					action: true
				})
				.then(response => {
					console.log(response);
					setCart(response.data); 
					setCartTotalPrice(response.data.cart_total_price);
					setCartTotalPromoPrice(response.data.cart_total_promo_price);
				})
				.catch(error => console.log(error))
			}}>
			Корзина пуста
			</button>
		);
	};

	return (
		<div>
			<div className="p-2">
				{cart.map((product, key) => 
					<div className="uk-transition-toggle" key={key}>
						<div className="uk-card-hover uk-transition-scale-up uk-transition-opaque d-flex border p-3" aria-hidden="true">
							
							<img src={MEDIA_SERVER_URL + product.image} alt={"Product " + product.id} 
							className="flex-shrink-0 me-3 my-auto rounded uk-transition-scale-up uk-transition-opaque" width="60" height="60" />
							<div className="row g-3">
								<div className="col-12">
									<a href="{% url 'product' %}?category=Корзина&id={{product.id}}" className="lead uk-button-text">{product.name}</a>
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
				<a type="button" className="btn-lg uk-button-text border-colored" href="{% url 'order' %}">Перейти к оформлению заказа</a>
			</div>
		</div>
	);
};

export default CartOffcanvas;