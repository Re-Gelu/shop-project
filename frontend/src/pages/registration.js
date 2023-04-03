import { useFormik } from 'formik';
import { signIn } from "next-auth/react";
import * as Yup from 'yup';
import Cookies from 'js-cookie';
import axios from '@/api.js';

const Registration = (props) => {

	async function onSubmit(data) {
		const response = await axios.post('auth/users/', data);
		if (response.status === 400) {
			for (const key in response.data) {
				for (const key2 in response.data[key]) {
					response.data[key][key2] = '- ' + response.data[key][key2] + '\n'
				};
			};
			formik.setErrors(response.data);
		} else if (response.status === 201) {
			signIn("credentials", {
				username: data.username,
				password: data.password,
				csrftoken: data.csrftoken, 
				callbackUrl: `${window.location.origin}/dashboard`
			});
		};
	};

	const formik = useFormik({
		initialValues: {
			username: "",
			first_name: "",
			last_name: "",
			password: "",
			password2: "",
			csrftoken: Cookies.get('csrftoken')
		},
		validationSchema: Yup.object({
			username: Yup.string()
				.min(1, 'Обязательное поле!')
				.max(30, 'Поле должно содержать меньше 30 символов!')
				.required('Обязательное поле!')
				.email('Это не адрес электронной почты!   :)'),
			password: Yup.string()
				.min(1, 'Обязательное поле!')
				.max(30, 'Поле должно содержать меньше 30 символов!')
				.required('Обязательное поле!'),
			password2: Yup.string()
				.min(1, 'Обязательное поле!')
				.max(30, 'Поле должно содержать меньше 30 символов!')
				.oneOf([Yup.ref('password'), null], 'Пароли не совпадают!')
				.required('Обязательное поле!'),
			first_name: Yup.string()
				.min(1, 'Обязательное поле!')
				.max(30, 'Поле должно содержать меньше 30 символов!')
				.required('Обязательное поле!'),
			last_name: Yup.string()
				.min(1, 'Обязательное поле!')
				.max(30, 'Поле должно содержать меньше 30 символов!')
				.required('Обязательное поле!'),
		}),
		onSubmit: values => {
			onSubmit(values);
		}
	});

	return (
		<div className="container col-md-5 col-12 p-3 p-xl-5 pt-5">
			<form className="row g-4 needs-validation" onSubmit={formik.handleSubmit}>
				
				<p className="h3 text-center">Регистрация</p>

				<hr />

				<input type="hidden" name="csrfmiddlewaretoken" value={Cookies.get('csrftoken')} />

				<div className="row form-row m-0"> 
					<div id="div_id_email" className="mb-3"> 
						<label htmlFor="id_email" className="form-label requiredField">
							Email адрес<span className="asteriskField">*</span> 
						</label> 
						<div> 
							<div className={formik.errors.username ? "input-group is-invalid" : "input-group"}> 
								<span className="input-group-text">
									<i className="bi bi-envelope"></i>
								</span> 
								<input type="email" name="username" maxLength="254" autoComplete='username'
									placeholder="email" 
									className={formik.errors.username ? "emailinput form-control is-invalid" : "emailinput form-control"}
									required={true} id="id_email" 
									{...formik.getFieldProps('username')}
								/> 
							</div>
							{formik.errors.username ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.username}</strong></div> : null}
						</div> 
					</div>

					<div className="form-group col-md-6"> 
						<div id="div_id_first_name" className="mb-3"> 
							<label htmlFor="id_first_name" className="form-label requiredField">
								Имя<span className="asteriskField">*</span> 
							</label> 
							<div> 
								<div className={formik.errors.first_name ? "input-group is-invalid" : "input-group"}> 
									<span className="input-group-text"><i className="bi bi-person"></i></span> 
									<input type="text" name="first_name" maxLength="150" 
										className={formik.errors.first_name ? "textinput textInput form-control is-invalid" : "textinput textInput form-control"} 
										required={true} id="id_first_name" 
										{...formik.getFieldProps('first_name')}
									/> 
								</div>
								{formik.errors.first_name ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.first_name}</strong></div> : null}
							</div> 
						</div> 
					</div> 
					<div className="form-group col-md-6"> 
						<div id="div_id_last_name" className="mb-3"> 
							<label htmlFor="id_last_name" className="form-label requiredField">
								Фамилия<span className="asteriskField">*</span> 
							</label> 
							<div> 
								<div className={formik.errors.last_name ? "input-group is-invalid" : "input-group"}> 
									<span className="input-group-text"><i className="bi bi-person-plus"></i></span> 
									<input type="text" name="last_name" maxLength="150" 
										className={formik.errors.last_name ? "textinput textInput form-control is-invalid" : "textinput textInput form-control"} 
										required={true} id="id_last_name" 
										{...formik.getFieldProps('last_name')}
									/> 
								</div>
								{formik.errors.last_name ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.last_name}</strong></div> : null}
							</div> 
						</div> 
					</div> 
				</div>
				<div className="row form-row m-0"> 
					<div className="form-group col-md-6"> 
						<div id="div_id_password1" className="mb-3"> 
							<label htmlFor="id_password1" className="form-label requiredField">
                				Пароль<span className="asteriskField">*</span> 
							</label> 
							<div> 
								<div className={formik.errors.password ? "input-group is-invalid" : "input-group"}> 
									<span className="input-group-text"><i className="bi bi-lock"></i></span> 
									<input type="password" name="password" autoComplete="new-password" 
										className={formik.errors.password ? "textinput textInput form-control is-invalid" : "textinput textInput form-control"}
										required={true} id="id_password" 
										aria-autocomplete="list" {...formik.getFieldProps('password')} /> 
								</div>
								{formik.errors.password ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.password}</strong></div> : null}
								<div id="hint_id_password1" className="form-text">
									<ul>
										<li>Пароль не должен быть слишком похож на другую вашу личную информацию.</li>
										<li>Ваш пароль должен содержать как минимум 8 символов.</li>
										<li>Пароль не должен быть слишком простым и распространенным.</li>
										<li>Пароль не может состоять только из цифр.</li>
									</ul>
								</div> 
							</div>
						</div> 
					</div> 
					<div className="form-group col-md-6"> 
						<div id="div_id_password2" className="mb-3"> 
							<label htmlFor="id_password2" className="form-label requiredField">
								Подтверждение пароля<span className="asteriskField">*</span> 
							</label> 
							<div> 
								<div className={formik.errors.password2 ? "input-group is-invalid" : "input-group"}> 
									<span className="input-group-text"><i className="bi bi-key"></i></span> 
									<input type="password" name="password2" autoComplete="new-password" 
										className={formik.errors.password2 ? "textinput textInput form-control is-invalid" : "textinput textInput form-control"}
										required={true} id="id_password2"
										{...formik.getFieldProps('password2')} /> 
								</div>
								{formik.errors.password2 ? <div className='invalid-feedback' style={{'whiteSpace': 'pre-line'}}><strong>{formik.errors.password2}</strong></div> : null}
								<div id="hint_id_password2" className="form-text">
									Для подтверждения введите, пожалуйста, пароль ещё раз.
								</div> 
							</div> 
						</div> 
					</div>
				</div>
				<div className="col-12 text-center mt-0"> 
					<div> 
						<hr />
						<button className="btn btn-lg uk-button-text m-2 px-5 border-colored" type="submit">
							Перейти к покупкам!
						</button> 
					</div>
				</div>
			</form>

		</div>
	)
};

export default Registration;