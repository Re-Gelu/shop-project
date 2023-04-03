import 'uikit/dist/css/uikit.min.css';
import 'uikit/dist/js/uikit.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@/styles/fonts.css'
import '@/styles/styles.css'
import { useEffect } from 'react';
import MainLayout from '@/components/MainLayout.js';
import Head from 'next/head';
import { SessionProvider } from "next-auth/react"


export default function App({ Component, pageProps: { session, ...pageProps } }) {

	useEffect(() => {
        import ('bootstrap/dist/js/bootstrap.min.js');
    }, []);

	return (
		<SessionProvider session={session}>
			<Head>
				<title>SITE_NAME</title>
			</Head>
			<MainLayout>
				<Component {...pageProps} />
			</MainLayout>
		</SessionProvider>
	)
}
