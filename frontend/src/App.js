import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
	{	
		path: "/",
		element: <div>Index page</div>,
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