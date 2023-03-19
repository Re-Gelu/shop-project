import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { ApiProvider } from './components/ApiContext';
import Base from './components/Base.js';
import Index from './components/Index.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import CartOffcanvas from './components/CartOffcanvas.js';

const router = createBrowserRouter([
	{	
		path: "/", 
		element: <Base />,
		children: [
			{
				path: "/",
				element: <Index />
			},
			{
				path: "/products",
				element: <div>products page</div>
			},
			{
				path: "/products/:category",
				element: <div>products page</div>,

			},
			{
				path: "/products/:category/:subcategory",
				element: <div>products page</div>
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