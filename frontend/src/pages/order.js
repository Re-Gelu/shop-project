import { useSession, signOut } from "next-auth/react";
import { useRouter } from "next/router";
import { useEffect, useState, useContext } from "react";

const OrderPage = () => {
    const { data: session, status } = useSession();
    const router = useRouter()

    if (status === "unauthenticated") {
		router.push('/login')
	};

    return (
		<div>Order page</div>
    )
};

export default OrderPage;