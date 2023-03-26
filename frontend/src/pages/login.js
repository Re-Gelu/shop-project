import Link from 'next/link';

const Login = (props) => {
	return (
		<div className="container col-xl-4 col-md-6 col-8 p-3 p-xl-5 pt-5">
			<form className="row g-4 needs-validation" method="post">

				<p className="h3 text-center">Вход</p>

				<hr />

				<p className="border border-2 my-2 lead p-2"> 
					Пожалуйста, используйте следующую форму для входа в систему. Если у вас до сих пор нет учетной записи 
					<Link className="text-decoration-underline ms-2" href="/registration">зарегистрируйтесь здесь!</Link>
				</p>

				<input type="hidden" name="next" value="{{next}}"/>

			</form>
		</div>
	);
};

export default Login;