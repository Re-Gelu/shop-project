import Link from 'next/link';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import Cookies from 'js-cookie';
import { signIn } from "next-auth/react";


const Login = (props) => {

	async function onSubmit(data) {
		console.log(data);
		signIn("credentials", {...data, callbackUrl: `${window.location.origin}/dashboard`});
	};

	const formik = useFormik({
		initialValues: {
			username: "",
			password: "",
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
				.required('Обязательное поле!')
		}),
		onSubmit: values => {
			onSubmit(values);
		}
	});

	return (
		<div className="container col-xl-4 col-md-6 col-8 p-3 p-xl-5 pt-5">
			<form className="row g-4 needs-validation" onSubmit={formik.handleSubmit}>

				<p className="h3 text-center">Вход</p>

				<hr />

				<p className="border border-2 my-2 lead p-2"> 
					Пожалуйста, используйте следующую форму для входа в систему. Если у вас до сих пор нет учетной записи 
					<Link className="text-decoration-underline ms-2" href="/registration">зарегистрируйтесь здесь!</Link>
				</p>

				<div className="form-row"> 
					<div id="div_id_login" className="mb-3"> 
						<label htmlFor="id_login" className="form-label requiredField">
                			Адрес электронной почты<span className="asteriskField">*</span> 
						</label> 
						<div> 
							<div className={formik.errors.username ? "input-group is-invalid" : "input-group"}> 
								<span className="input-group-text">
									<i className="bi bi-envelope"></i>
								</span> 
								<input type="text" name="username" autoFocus={true} autoComplete="current-login" placeholder="email" 
								className={formik.errors.username ? "emailinput form-control is-invalid" : "emailinput form-control"}
								required={true} id="id_login" {...formik.getFieldProps('username')}/>
							</div> 
							{formik.errors.username ? <div className='invalid-feedback'><strong>{formik.errors.username}</strong></div> : null}
						</div> 
					</div> 
					<div id="div_id_password" className="mb-3"> 
						<label htmlFor="id_password" className="form-label requiredField">
							Пароль<span className="asteriskField">*</span> 
						</label> 
						<div> 
							<div className={formik.errors.password ? "input-group is-invalid" : "input-group"}> 
								<span className="input-group-text">
									<i className="bi bi-lock"></i>
								</span> 
								<input type="password" name="password" placeholder=" " autoComplete="current-password" 
									className={formik.errors.password ? "textinput textInput form-control is-invalid" : "textinput textInput form-control"}
									required="" id="id_password" {...formik.getFieldProps('password')}
								/>
							</div>
							{formik.errors.password ? <div className='invalid-feedback'><strong>{formik.errors.password}</strong></div> : null}
						</div> 
					</div>
					<div className="mb-3"> 
						<div id="div_id_remember" className="mb-3 form-check"> 
							<input type="checkbox" name="remember" value={'on'} checked={true}
							className="background-colored border-colored checkboxinput form-check-input" id="id_remember"  {...formik.getFieldProps('remember')}/> 
							<label htmlFor="id_remember" className="form-check-label">Запомнить меня</label> 
						</div> 
					</div> 
				</div>

				<input type="hidden" name="csrfmiddlewaretoken" value={Cookies.get('csrftoken')} />

				<div className="col-12 text-center mt-0"> 
					<hr />
					<button className="btn btn-lg uk-button-text m-2 px-5 border-colored" type="submit">Войти</button> 
				</div>

			</form>
		</div>
	);
};

export default Login;