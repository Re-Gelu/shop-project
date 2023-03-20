import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { ApiProvider } from './components/ApiContext';
import Base from './components/Base.js';
import IndexPage from './components/IndexPage.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import CartOffcanvas from './components/CartOffcanvas.js';
import ProductPage from './components/ProductPage.js';
import ShopPage from './components/ShopPage.js';

const router = createBrowserRouter([
	{	
		path: "/", 
		element: <Base />,
		children: [
			{
				path: "/",
				element: <IndexPage />
			},
			{
				path: "/product/:productID",
				element: <ProductPage />
			},
			{
				path: "/products",
				element: <ShopPage />
			},
			{
				path: "/products/:category",
				element: <ShopPage />,

			},
			{
				path: "/products/:category/:subcategory",
				element: <ShopPage />
			},
		],
	},
	{
		path: "/contacts",
		element: <div>Contacts page</div>
	},
	{
		path: "/delivery",
		element: <div>Delivery page</div>
	},
	{
		path: "/about",
		element: <div>About page</div>
	},
	{
		path: "/dashboard",
		element: <div>Dashboard page</div>
	},
]);

const App = () => {
  	return (
		<ApiProvider>
			<Header />
			<CartOffcanvas />
			<RouterProvider router={router} />
			<Footer />
		</ApiProvider>
	);
}

export default App;