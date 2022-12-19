jQuery(document).ready( () => {

$.ajaxSetup({
    "headers": {
        "X-CSRFToken": csrf_token
    }
})

const basic_url =  window.location.protocol + '//' + window.location.host + '/'

/* DASHBOARD BUTTONS EVENT HANDLERS */

/* Event handler to add one piece of product in dashboard cart */
document.querySelectorAll('[id=cart-dashboard-add-one-btn]').forEach( (element) => {
    element.onclick = () => {
        const product_id = parseInt(element.getAttribute("product-id"))

        const data = {
            "id": product_id,
            "action": true,
            "amount": 1,
        }

        $.post(
            basic_url + 'api/cart/',
            data,
            (data, textStatus) => {
                console.log(textStatus, data);
                $('#dashboard-cart').load(basic_url + 'api/dashboard_cart/');
            }
        );
    };
});

/* Event handler to remove one piece of product from dashboard cart */
document.querySelectorAll('[id=cart-dashboard-remove-one-btn]').forEach( (element) => {
    element.onclick = () => {
        const product_id = parseInt(element.getAttribute("product-id"))

        const data = {
            "id": product_id,
            "action": false,
            "amount": 1
        }

        $.post(
            basic_url + 'api/cart/',
            data,
            (data, textStatus) => {
                console.log(textStatus, data);
                $('#dashboard-cart').load(basic_url + 'api/dashboard_cart/');
            }
        );
    };
});

/* Event handler to remove one product position from dashboard cart */
document.querySelectorAll('[id=cart-dashboard-remove-btn]').forEach( (element) => {
    element.onclick = () => {
        const product_id = parseInt(element.getAttribute("product-id"))

        const data = {
            "id": product_id,
            "action": false,
            "amount": 100
        }

        $.post(
            basic_url + 'api/cart/',
            data,
            (data, textStatus) => {
                console.log(textStatus, data);
                $('#dashboard-cart').load(basic_url + 'api/dashboard_cart/');
            }
        );
    };
});

});