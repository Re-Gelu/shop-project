import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import CartOffcanvas from './components/CartOffcanvas.js';
import reportWebVitals from './reportWebVitals';
import 'uikit/dist/css/uikit.min.css';
import 'uikit/dist/js/uikit.min.js';
import 'uikit/dist/js/uikit-icons.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import './fonts.css'
import './styles.css'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
	<React.StrictMode>
		<App />
  	</React.StrictMode>
);

ReactDOM.createRoot(document.getElementById('cart-offcanvas-body')).render(
	<CartOffcanvas />
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
