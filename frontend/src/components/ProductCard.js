import { useContext } from "react";
import { ApiContext } from '@/components/ApiContext.js';
import Link from 'next/link';


const ProductCard = ({ product, cardAnimationClass }) => {

    const {cartEventHandler} = useContext(ApiContext);

    return (
        <>
        {product && (
            <div id="product-card" className="h-100 uk-transition-toggle">
            <div className={`card h-100 uk-card-hover uk-transition-opaque ${cardAnimationClass || "uk-transition-scale-up"}`} aria-hidden="true">
                {/* Product card image */}
                <img
                id="product-img"
                src={product.image}
                className="card-img-top img-rounded h-100 uk-object-scale-down p-2 uk-transition-opaque"
                alt="Product"
                />

                {/* Product card body */}
                <div className="card-body">
                {product.promo_price ? (
                    <div className="uk-card-badge background-colored">Скидка!</div>
                ) : product.was_publiched_recently ? (
                    <div className="uk-card-badge uk-label">Новинка!</div>
                ) : null}
                <div className="card-title h5">{product.name}</div>
                <div className="card-text overflow-hidden">
                    <span>{product.information}</span>
                    <p className="my-2">
                    {product.promo_price ? (
                        <>
                        <span className="me-3 text-reset lead text-decoration-line-through">{product.price}</span>
                        <span className="me-3 lead text-danger">{product.promo_price} RUB</span>
                        </>
                    ) : (
                        <span className="me-3 text-reset lead">{product.price} RUB</span>
                    )}
                    <span className="d-inline-flex">
                        <i className="bi bi-heart me-1"></i>
                        <i className="bi bi-chat-square me-1"></i>
                        <i className="bi bi-star me-1"></i>
                    </span>
                    </p>
                </div>

                <div className="card-footer d-flex bg-white row">
                    <div className="my-2 col-9">
                    <Link href={`/product/${product.id}`} className="uk-button-text a-important">
                        ПОДРОБНЕЕ
                    </Link>
                    </div>
                    {(!product.available || product.stock === 0) ? (
                    <div className="my-2 p-0 col-3">
                        <button type="submit" className="btn btn-outline-secondary uk-button-text text-decoration-line-through col-12">
                            <i className="bi bi-cart-x"></i>
                        </button>
                    </div>
                    ) : (
                    <div className="my-2 p-0 col-3">
                        <button type="submit" id="cart-add-one-btn" product-id={product.id} className="btn btn-dark text-white background-colored col-12"
                        onClick={(e) => cartEventHandler(e, {"id": product.id, "action": true, "amount": 1})}>
                            <i className="bi bi-cart"></i>
                        </button>
                    </div>
                    )}
                </div>
                </div>
            </div>
            </div>
        )}
        </>
    );
}

export default ProductCard;