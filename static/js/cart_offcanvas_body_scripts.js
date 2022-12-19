jQuery(document).ready( () => {

$.ajaxSetup({
    "headers": {
        "X-CSRFToken": csrf_token
    }
})

const basic_url =  window.location.protocol + '//' + window.location.host + '/'

/* HEADER OFFCANVAS BUTTONS EVENT HANDLERS */

/* Event handler to add one piece of product in offcanvas cart */
document.querySelectorAll('[id=cart-offcanvas-add-one-btn]').forEach( (element) => {
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
                $('#cart-offcanvas-body').load(basic_url + 'api/header_offcanvas_body/');
            }
        );
    };
});

/* Event handler to remove one piece of product from cart */
document.querySelectorAll('[id=cart-offcanvas-remove-one-btn]').forEach( (element) => {
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
                $('#cart-offcanvas-body').load(basic_url + 'api/header_offcanvas_body/');
            }
        );
    };
});

/* Event handler to remove one product position from cart */
document.querySelectorAll('[id=cart-offcanvas-remove-btn]').forEach( (element) => {
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
                $('#cart-offcanvas-body').load(basic_url + 'api/header_offcanvas_body/');
            }
        );
    };
});

});