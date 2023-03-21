import { useRouter } from 'next/router';
import { useContext } from "react";
import { ApiContext } from '@/components/ApiContext.js';

const ProductPageCard = ({product}) => {
    const router = useRouter();
    const {cartEventHandler} = useContext(ApiContext);

    if (router.isFallback) {
		return <div>Загрузка...</div>
	};

    return (
        <article className="row mt-1">
            <section id="product-card" className="row mt-1">
                {/* Product image */}
                <div id="product-img" className="col-xl-7 uk-transition-toggle text-center">
                    <img
                        src={product.image}
                        className="h-100 uk-object-scale-down p-2 uk-transition-opaque uk-transition-scale-up img-rounded"
                        alt="Product" />
                    </div>
                    {/* Product price */}
                    <div className="col-xl-5 lead text-center my-auto">
                        {product.promo_price ? (
                            <>
                                Стоимость:
                                <span className="mx-2 text-reset lead text-decoration-line-through">
                                    {product.price} RUB
                                </span>
                                <span className="lead text-danger">
                                    {product.promo_price} RUB
                                </span>
                            </>
                        ) : (
                            <>
                                Стоимость:
                                <span className="text-reset lead ms-2">{product.price} RUB</span>
                            </>
                        )}

                        <div className="m-3">
                            {(!product.available || product.stock === 0) ? (
                            <button className="btn btn-lg btn-outline-secondary uk-button-text text-decoration-line-through">
                                Добавить в корзину <i className="bi bi-cart"></i>
                            </button>
                            ) : (
                            <button
                                id="cart-add-one-btn"
                                product-id={product.id}
                                className="btn btn-lg uk-button-text border-colored"
                                onClick={(e) => cartEventHandler(e, {"id": product.id, "action": true, "amount": 1})}
                            >
                                Добавить в корзину <i className="bi bi-cart"></i>
                            </button>
                            )}
                        </div>

                        <div>
                            {(!product.available || product.stock === 0) ? (
                                <span className="text-colored">Товара нет в наличии!</span>
                            ) : product.stock < 5 ? (
                                <span className="text-colored">Товара осталось меньше 5шт!</span>
                            ) : product.stock < 10 ? (
                                <span className="text-colored">Товара осталось меньше 10шт!</span>
                            ) : null}
                        </div>
                    </div>
            </section>

            <section className="row mt-1">
                <div className="col-xl-7 m-2 my-3 text-center">
                {/* Product name */}
                <h5 className="lead fs-3">{product.name}</h5>

                {/* Product information */}
                <div className="my-3">{product.information}</div>
                </div>

                <div className="col-xl-10">
                {product.full_information ? (
                    <div dangerouslySetInnerHTML={{ __html: product.full_information }} />
                ) : (
                    <div className="lead m-5">Описание отсутвует</div>
                )}
                </div>
            </section>
        </article>
    );
};

export default ProductPageCard;