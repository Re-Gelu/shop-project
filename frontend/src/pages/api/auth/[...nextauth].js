import NextAuth from "next-auth";
import jwtDecode from "jwt-decode";
import CredentialsProvider from "next-auth/providers/credentials";
import axios from '@/api.js';
import { BASE_URL } from '@/config.js';

async function refreshAccessToken(token) {
	try {
		const response = await axios.post('auth/jwt/refresh/', {"refresh": token.refresh});
		const refreshedAccessToken = response.data;
		if (response.status !== 200) throw refreshedAccessToken.access;
		const { user_id, exp, jti, iat } = jwtDecode(refreshedAccessToken.access);
		return {
			...token,
			...refreshedAccessToken,
			exp,
			jti,
			iat,
			user: {
				user_id
			},
		};
	} catch (error) {
		return {
			...token,
			error: "RefreshAccessTokenError",
		};
	}
};

export const authOptions = {
	site: BASE_URL,
	providers: [
		CredentialsProvider({
			name: "Django Rest Framework",
			credentials: {
				username: {
					label: "Username",
					type: "username",
					placeholder: "username",
				},
				password: { 
					label: "Password", 
					type: "password" 
				},
			},
			async authorize(credentials) {
				try {
					const response = await axios.post('auth/jwt/create/', credentials);
					const token = response.data;
					if (response.status !== 200) throw token;
					const { user_id, exp, jti } = jwtDecode(token.access);
					return {
						...token,
						exp,
						jti,
						user: {
							user_id
						},
					};
				} catch (error) {
					return null;
				}
			},
		}),
	],
	pages: {
		signIn: '/login',
		signOut: '/',
		error: '/login',
		newUser: '/register'
	},
	callbacks: {
		async redirect({ url, baseUrl }) {
			return url.startsWith(baseUrl)
			? Promise.resolve(url)
			: Promise.resolve(baseUrl);
		},
		async jwt({ token, user, account, profile, isNewUser }) {
			// initial signin
			if (account && user) {
				return user;
			}

			// Return previous token if the access token has not expired
			if (Date.now() < token.exp * 100) {
				return token;
			}

			// refresh token
			return refreshAccessToken(token);
		},
		async session({ session, token }) {
			session.user = token.user;
			session.access = token.access;
			session.refresh = token.refresh;
			session.exp = token.exp;
			return session;
		},
	},
	session: { 
		jwt: true,
		strategy: "jwt" 
	},
	debug: true,
}

export default NextAuth(authOptions)