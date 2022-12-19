jQuery(document).ready( () => {

$.ajaxSetup({
    "headers": {
        "X-CSRFToken": csrf_token
    }
});

const basic_url =  window.location.protocol + '//' + window.location.host + '/';


/* CART BUTTONS EVENT HANDLERS */


const event = (data, textStatus) => {
    console.log(textStatus, data);
    $('#dashboard-cart').load(basic_url + 'api/dashboard_cart/');
    $('#cart-offcanvas-body').load(basic_url + 'api/header_offcanvas_body/');
};

const cart_event_handler = (ids, data) => {

    document.querySelectorAll(ids).forEach( (element) => {
        element.onclick = () => {
            $.post(
                basic_url + 'api/cart/',
                $.extend(
                    {"id": parseInt(element.getAttribute("product-id"))},
                    data
                ),
                event
            );
        };
    });

};

/* Event handler to add one piece of product in cart */
cart_event_handler(
    ids='\
        #cart-add-one-btn, \
        #cart-dashboard-add-one-btn, \
        #cart-offcanvas-add-one-btn',
    data={
        "action": true,
        "amount": 1,
    }
);

/* Event handler to remove one piece of product from cart */
cart_event_handler(
    ids='\
        #cart-remove-one-btn, \
        #cart-dashboard-remove-one-btn, \
        #cart-offcanvas-remove-one-btn',
    data={
        "action": false,
        "amount": 1
    }
);

/* Event handler to remove one product position from cart */
cart_event_handler(
    ids='\
        #cart-remove-btn, \
        #cart-dashboard-remove-btn, \
        #cart-offcanvas-remove-btn',
    data={
        "action": false,
        "amount": 100
    }
);

});