import { useSession } from "next-auth/react";
import { useRouter } from "next/router";
import { useContext } from "react";
import { ApiContext } from '@/components/ApiContext.js';
import Link from 'next/link';
import { MEDIA_SERVER_URL } from "@/config.js";
import Cookies from 'js-cookie';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from '@/api.js';


const OrderPage = (props) => {
    const { data: session, status } = useSession();
    const router = useRouter();
    const { 
		cart, 
		cartTotalPrice,
		cartTotalPromoPrice, 
	} = useContext(ApiContext);

	async function onSubmit(data) {
		console.log(data);
		const response = await axios.post('orders/', data);
		if (response.status === 400) {
			for (const key in response.data) {
				for (const key2 in response.data[key]) {
					response.data[key][key2] = '- ' + response.data[key][key2] + '\n'
				};
			};
			formik.setErrors(response.data);
		} else if (response.status === 201) {
			router.push(response.data.payment_link);
		};
	};

	const phoneRegExp = /^((\+[1-9]{1,4}[ -]?)|(\([0-9]{2,3}\)[ -]?)|([0-9]{2,4})[ -]?)*?[0-9]{3,4}[ -]?[0-9]{3,4}$/

	const formik = useFormik({
		initialValues: {
			email: "",
			adress: "",
			phone_number: "",
			csrftoken: Cookies.get('csrftoken')
		},
		validationSchema: Yup.object({
			email: Yup.string()
				.required('Обязательное поле!')
				.email('Это не адрес электронной почты!   :)'),
			adress: Yup.string()
				.max(200, 'Поле должно содержать меньше 200 символов!')
				.required('Обязательное поле!'),
			phone_number: Yup.string()
				.matches(phoneRegExp, {
					message: 'Это не номер телефона!   :)',
					excludeEmptyString: false,
				})
				.required('Обязательное поле!')
				.max(20, 'Поле должно содержать меньше 20 символов!')
			}),
		onSubmit: values => {
			onSubmit(values);
		}
	});

    if (status === "unauthenticated") {
		router.push('/login')
	};

    return (
		<div className="container col-xl-6 col-lg-8 col-md-8 col-12 p-5">
			<form className="row g-4 needs-validation" onSubmit={formik.handleSubmit}>
				<p className="h3 text-center">Оформление заказа</p>
				<input type="hidden" name="csrfmiddlewaretoken" value={Cookies.get('csrftoken')} />
				<hr />
				<table className="uk-table uk-table-divider uk-table-middle text-center">
					<thead>
						<tr>
						<th className="text-center">Товар</th>
						<th className="text-center">Кол-во</th>
						<th className="text-center">Цена за шт.</th>
						<th className="text-center">Итоговая цена</th>
						</tr>
					</thead>
					<tbody>
						{cart && Object.keys(cart).length > 0 && cart.map((product) => (
							<tr key={product.id}>
								<td>
									<Link href={`product/${product.id}/`}
									className="d-inline-flex" >
										<img src={MEDIA_SERVER_URL + product.image}
										alt={"Product " + product.id}
										width="60px"
										className="flex-shrink-0 me-2 my-auto rounded" />
										<div className="my-auto ms-2">{product.name}</div>
									</Link>
								</td>
								<td>{product.product_amount}</td>
								<td>
								{product.promo_price ? (
									<>
										<div className="text-decoration-line-through">{product.price} RUB</div>
										<div className="text-danger">{product.promo_price} RUB</div>
									</>
								) : (
									`${product.price} RUB`
								)}
								</td>
								<td>
								{product.total_promo_price ? (
									<>
										<div className="text-decoration-line-through">{product.total_price} RUB</div>
										<div className="text-danger">{product.total_promo_price} RUB</div>
									</>
								) : (
									`${product.total_price} RUB`
								)}
								</td>
							</tr>
						))}
						<tr>
						<td>Итого:</td>
						<td colSpan="2"></td>
						<td>
							{cartTotalPromoPrice < cartTotalPrice ? (
								<>
									<span className="text-decoration-line-through me-2">{cartTotalPrice} RUB</span>
									<span className="text-danger">{cartTotalPromoPrice} RUB</span>
								</>
							) : (
								<>{cartTotalPrice} RUB</>
							)}
						</td>
						</tr>
					</tbody>
				</table>

				<div className="form-row">
					<div id="div_id_email" className="mb-3"> 
						<label htmlFor="id_email" className="form-label requiredField">
							Email<span className="asteriskField">*</span> 
						</label> 
						<div> 
							<div className={formik.errors.email ? "input-group is-invalid" : "input-group"}> 
								<span className="input-group-text">@</span> 
								<input type="email" name="email" maxLength="40" placeholder="email" 
								className={formik.errors.email ? "emailinput form-control is-invalid" : "emailinput form-control"} 
								required={true} id="id_email" {...formik.getFieldProps('email')}/> 
							</div> 
							{formik.errors.email ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.email}</strong></div> : null}
						</div> 
					</div> 
					<div id="div_id_adress" className="mb-3"> 
						<label htmlFor="id_adress" className="form-label requiredField">
							Адрес<span className="asteriskField">*</span> 
						</label> 
						<input type="text" name="adress" maxLength="500" 
						className={formik.errors.adress ? "textinput textInput form-control is-invalid" : "textinput textInput form-control"} 
						required={true} id="id_adress" {...formik.getFieldProps('adress')}/>
						{formik.errors.adress ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.adress}</strong></div> : null}
					</div>
					<div id="div_id_phone_number" className="mb-3"> 
						<label htmlFor="id_phone_number" className="form-label requiredField">
							Номер телефона<span className="asteriskField">*</span> 
						</label> 
						<input type="tel" name="phone_number" placeholder="+76665554433" 
						className={formik.errors.phone_number ? "form-control is-invalid" : " form-control"}
						required={true} id="id_phone_number" {...formik.getFieldProps('phone_number')} />
						{formik.errors.phone_number ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.phone_number}</strong></div> : null}
					</div>
				</div>

				<div className="col-12 text-center mt-0"> 
					<div> 
						<hr />
						<button className="btn btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Перейти к оплате</button> 
					</div>
				</div>

				<div className="col-12 text-center">
					<p className="small a-important mb-1">
						Время на оплату: 30 мин
					</p>
					<p className="small a-important">
						Платеж обрабатывается в течении минуты
					</p>
				</div>
			</form>
    	</div>
    )
};

export default OrderPage;