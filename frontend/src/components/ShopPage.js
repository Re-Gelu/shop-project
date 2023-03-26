import ProductCard from "@/components/ProductCard.js";
import TopRow from "@/components/TopRow.js";
import Pagination from "@/components/Pagination.js";

const ProductPage = (props) => {
    const {
        products,
        total_pages,
        page
    } = {...props};

    return (
        <div className="row mt-1 g-2">
            <TopRow {...props}/>
            
            {products &&  (products.length !== 0) ? (
                <>
                    {products.map((product) => (
                        <div className="col-xl-3" key={product.id}>
                            <ProductCard product={product} />
                        </div>
                    ))}
                    <Pagination 
                        currentPage={page}
                        totalPages={total_pages}
                        {...props}
                     />
                </>
            )
            : (
                /* <!-- No products in category --> */
                <div className="container col-xl-5 col-12 p-5">
                    <div className="row g-3 text-center">
                        <p className="h2">Товаров пока нет!</p>
                        <hr />
                        <p>Возможно когда нибудь я их даже добавлю (но это не точно)</p>
                    </div>
                </div>
            )
            }
        </div>
    );
};

export default ProductPage;