import { createContext, useState, useEffect } from 'react';
import $ from 'jquery';
import axios from '@/api';

const ApiContext = createContext();

/* Cart animation */
const cart_animation = (element) => {
    var img = $(element).closest('#product-card').find('#product-img');
    var cart = $("#shopping-cart-offcanvas-open-button");
    var offset = img.offset();
    img.clone()
    .removeClass('card-img-top h-100 uk-object-scale-down p-2 uk-transition-opaque')
    .css({
        'width':img.width(),
        'position':'absolute',
        'z-index':'9999',
        top:offset.top,
        left:offset.left
    })
    .appendTo("body")
    .animate({opacity: 0.05,
        left: cart.offset()['left'],
        top: cart.offset()['top'],
        width: 20}, 1000, 
        function() {
            $(this).remove();
        }
    );
};

const ApiProvider = ({ children }) => { 
    const [cart, setCart] = useState({});
	const [cartTotalPrice, setCartTotalPrice] = useState(0);
	const [cartTotalPromoPrice, setCartTotalPromoPrice] = useState(0);

    useEffect(() => {
        axios.get('cart')
        .then(response => {
            setCart(response.data.cart);
            setCartTotalPrice(response.data.cart_total_price);
            setCartTotalPromoPrice(response.data.cart_total_promo_price);
        })
        .catch(error => console.log(error));
    }, [setCart]);

    const cartEventHandler = (e, data) => {
		axios.post('cart/', data)
		.then(response => {
            console.log(response.data);
			setCart(response.data.cart);
			setCartTotalPrice(response.data.cart_total_price);
			setCartTotalPromoPrice(response.data.cart_total_promo_price);
		})
		.catch(error => console.log(error));
		if (
            (e.target.getAttribute("id") || 
            e.target.parentElement.getAttribute("id") === "cart-add-one-btn") &&
            e.target.getAttribute("id") !== "cart-offcanvas-remove-btn" &&
            e.target.getAttribute("id") !== "cart-dashboard-remove-btn"
        ) {
			cart_animation(e.target);
		};
	};

    const contextValue = {
        cart, 
        setCart, 
        cartTotalPrice, 
        setCartTotalPrice, 
        cartTotalPromoPrice, 
        setCartTotalPromoPrice, 
        cartEventHandler
    };

    return (
        <ApiContext.Provider value={contextValue}>
            {children}
        </ApiContext.Provider>
  );
};

export { ApiContext, ApiProvider };
