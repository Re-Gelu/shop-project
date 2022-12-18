jQuery(document).ready( () => {

$.ajaxSetup({
    "headers": {
        "X-CSRFToken": csrf_token
    }
})

const basic_url =  window.location.protocol + '//' + window.location.host + '/'
    
/* Event handler to add one piece of product in cart */
document.querySelectorAll('[id=cart-add-one-btn]').forEach( (element) => {
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
                $('body').load(document.location.href);
            }
        );
    };
});

/* Event handler to remove one piece of product from cart */
document.querySelectorAll('[id=cart-remove-one-btn]').forEach( (element) => {
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
                $('body').load(document.location.href);
            }
        );
    };
});

/* Event handler to remove one product position from cart */
document.querySelectorAll('[id=cart-remove-btn]').forEach( (element) => {
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
                $('body').load(document.location.href);
            }
        );
    };
});

});