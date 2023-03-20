import { ApiProvider } from '@/components/ApiContext';
import Header from '@/components/Header.js';
import Footer from '@/components/Footer.js';
import CartOffcanvas from '@/components/CartOffcanvas.js';

const MainLayout = ({ children }) => {
    return (
		<ApiProvider>
			<Header />
			<CartOffcanvas />
			{children}
			<Footer />
     	 </ApiProvider>
    )
};

export default MainLayout;