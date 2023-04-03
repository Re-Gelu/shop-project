import { useSession, signOut } from "next-auth/react";
import { useRouter } from "next/router";
import { useEffect, useState, useContext } from "react";
import { ApiContext } from '@/components/ApiContext.js';
import React from "react";
import Link from 'next/link';
import { MEDIA_SERVER_URL } from "@/config.js"
import axios from '@/api.js';


const Dashboard = (props) => {
	const { data: session, status } = useSession();
	const router = useRouter()
	const [user, setUser] = useState({});
	const [currentOrders, setCurrentOrders] = useState([]);
	const { 
		cart, 
		cartTotalPrice,
		cartTotalPromoPrice, 
		cartEventHandler
	} = useContext(ApiContext);


	if (status === "unauthenticated") {
		router.push('/login')
	};

	useEffect(() => {
		if (status === "authenticated") {
			try {
				axios.get('auth/users/me')
				.then(response => {
					setUser(response.data);	
				});
				axios.get(`orders/?user_id=${session.user.user_id}&page_size=6`)
				.then(response => {
					setCurrentOrders(response.data.results);
				});
			} catch (e) {
				console.log(e);
			}
		};
	}, [status]);

	return (
		<article>
			<section className="row m-0">
				<div className="container col-xl-6 col-lg-8 col-md-8 col-12 p-3 pt-5">
					<div className="g-3 text-center">
						<p className="h2">Личный кабинет</p>
						<hr />
						<p className="lead">Привет{user && user.first_name && user.first_name.length > 0 && `, ${user.first_name}`}</p>
					</div>
				</div>
			</section>

			{(currentOrders.length > 0) && (
				<section className="row m-0 px-4">
					<p className="h3 text-center">Ваши заказы</p>
					<div className="container col-xxl-8 col-12 p-0 mt-0 mb-3 g-3 text-center uk-overflow-auto">
						<table className="uk-table uk-table-middle uk-table-divider uk-table-responsive">
						<thead>
							<tr>
							<th className="text-center">UUID заказа</th>
							<th className="text-center">Статус оплаты</th>
							<th className="text-center">Список товаров</th>
							<th className="text-center">Адрес</th>
							<th className="text-center">Контакты</th>
							<th className="text-center">Дата создания заказа</th>
							</tr>
						</thead>
						<tbody>
							{currentOrders.map((order) => (
								<tr key={order.id}>
									<td>{order.order_UUID}</td>
									<td>{order.status}</td>
									<td>
										<pre className="p-0 border-0">{order.order_info}</pre>
									</td>
									<td>{order.adress}</td>
									<td>{order.contacts}</td>
									<td>{new Date(order.created).toLocaleDateString("ru")}</td>
								</tr>
							))}
						</tbody>
						</table>
					</div>
				</section>
			)}

			<div id="dashboard-cart">
				{(Object.keys(cart).length > 0) && <section className="row m-0">
					<div id="cart-container" className="container col-xl-6 col-lg-10 col-md-12 col-12 p-0">
						<div className="g-3 text-center">
							<p className="h3">Корзина</p>
							<table className="uk-table uk-table-middle uk-table-divider uk-overflow-auto">
								<thead>
									<tr>
										<th className="text-center">Товар</th>
										<th className="text-center">Кол-во</th> 
										<th className="text-center d-md-table-cell d-none">Цена за шт.</th>
										<th className="text-center">Итоговая цена</th>
									</tr>
								</thead>
								<tbody>
									{cart.map((product) => (
										<tr key={product.id}>
											<td className="uk-transition-toggle">
												<Link href={`product/${product.id}/`} 
												className=" d-inline-flex">
													<img src={MEDIA_SERVER_URL + product.image} alt={"Product " + product.id}  width="60px" 
													className="rounded uk-transition-scale-up uk-transition-opaque" />
													<div className="my-auto ms-2">{product.name}</div>
												</Link>
											</td>

											<td>
												<div className="row col-12 m-0">

													<div className="col-4 p-0">
														<button id="cart-dashboard-remove-one-btn" product-id={product.id} className="col-4 border-0 p-0 bg-transparent" 
															onClick={(e) => cartEventHandler(e, {"id": product.id, "action": false,"amount": 1})}>
															<i className="bi bi-dash-lg"></i>
														</button>
													</div>

													<span id={`product_amount_for_id_${product.id}`} className="col-4 p-0">{product.product_amount}</span>

													<div className="col-4 p-0">
														<button id="cart-dashboard-add-one-btn" product-id={product.id} className="col-4 border-0 p-0 bg-transparent" 
															onClick={(e) => cartEventHandler(e, {"id": product.id, "action": true, "amount": 1})}>
															<i className="bi bi-plus-lg"></i>
														</button>
													</div>

												</div>
											</td>

											<td className="d-md-table-cell d-none">
												{product.promo_price ?
													<div>
														<div className="text-decoration-line-through">{product.price} RUB</div>
														<div className="text-danger">{product.promo_price} RUB</div>
													</div>
												:
													`${product.price} RUB`
												}
											</td>

											<td>
												{product.total_promo_price ?
													<div>
														<div className="text-decoration-line-through">{product.total_price} RUB</div>
														<div className="text-danger">{product.total_promo_price} RUB</div>
													</div>
												:
													`${product.total_price} RUB`
												}
											</td>

											<td className="uk-table-shrink ps-0 uk-width-min-content">
												<button id="cart-dashboard-remove-btn" product-id={product.id} className="btn-close btn-sm btn-lg float-end" aria-label="Delete product"
												onClick={(e) => cartEventHandler(e, {"id": product.id, "action": false,"amount": 100})}></button>
											</td>

										</tr>
									))}

									<tr>
										<td>Итого:</td>
										<td colSpan="2" className="d-md-table-cell d-none"></td>
										<td>
											{(cartTotalPromoPrice < cartTotalPrice) ? (
												<div>
													<span className="text-decoration-line-through me-2">{cartTotalPrice} RUB</span>
													<span className="text-danger">{cartTotalPromoPrice} RUB</span>
												</div>
											) : (
												`${cartTotalPrice} RUB`
											)}
										</td>
									</tr>

								</tbody>
							</table>
							<div className="row my-3">
								<div className="col-3"></div>
									<a type="button" className="btn btn-lg uk-button-text border-colored col-6">Перейти к оформлению заказа</a>
								<div className="col-3"></div>
							</div>
						</div>
					</div>
				</section>}
			</div>

			<section className="row m-0">
				<div className="container col-xl-6 col-lg-8 col-md-8 col-12 p-3">
					<nav className="g-3 text-center">
						{user && user.is_superuser && (
							<React.Fragment>
								<p>
								<a
									className="text-reset uk-button-text a-important lead"
									href={`${MEDIA_SERVER_URL}/admin`}
								>
									Админ-панель
								</a>
								</p>
								<p>
								<a
									className="text-reset uk-button-text a-important lead"
									href={`${MEDIA_SERVER_URL}/swagger`}
								>
									API swagger
								</a>
								</p>
							</React.Fragment>
						)}
						<p>
							<a
								className="text-reset uk-button-text a-important lead"
								href="/password_change">
								Сменить пароль
							</a>
						</p>
						<p>
						<a
							className="text-reset uk-button-text a-important lead"
							href="#"
							onClick={() => signOut()}>
							Выйти
						</a>
					</p>
					</nav>
				</div>
			</section>
		</article>
	);
};

export default Dashboard;