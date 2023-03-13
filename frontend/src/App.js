import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Base from './components/Base.js';
import Index from './components/Index.js';

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

function App() {
  	return (<RouterProvider router={router} />);
}

export default App;