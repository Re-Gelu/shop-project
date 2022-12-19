jQuery(document).ready( () => {

$.ajaxSetup({
    "headers": {
        "X-CSRFToken": csrf_token
    }
});

const basic_url =  window.location.protocol + '//' + window.location.host + '/';


/* Cart buttons event handler */
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

            if (element.getAttribute("id") === "cart-add-one-btn") {
                cart_animation(element);
            }
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


/* Cart animation */
const cart_animation = (element) => {
    var img = $(element).closest('#product-card').find('#product-img');
    var cart = $("#shopping-cart-offcanvas-open-button");
    img.clone()
        .removeClass('card-img-top h-100 uk-object-scale-down p-2 uk-transition-opaque')
        .css({'width' : img.width(),
            'position' : 'absolute',
            'z-index' : '9999',
            top: img.offset().top,
            left:img.offset().left})
        .appendTo("body")
        .animate({opacity: 0.05,
            left: cart.offset()['left'],
            top: cart.offset()['top'],
            width: 20}, 1000, function() {	
            $(this).remove();
        });
};

});