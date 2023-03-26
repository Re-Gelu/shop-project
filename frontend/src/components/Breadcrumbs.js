import { useRouter } from 'next/router';
import Link from 'next/link';

const Breadcrumbs = (props) => {
	let {
		categories,
		subcategories,
        category,
        subcategory,
        page,
		product
    } = {...props};
	const router = useRouter();
	const searchQuery = router.query.searchQuery;

	if (product === undefined) {
		category = categories.filter(oneOfCategories => oneOfCategories.id === parseInt(category))[0];
		subcategory = subcategories.filter(oneOfSubcategories => oneOfSubcategories.id === parseInt(subcategory))[0];
	} else {
		category = categories.filter(oneOfCategories => oneOfCategories.id === parseInt(product.category))[0];
		subcategory = subcategories.filter(oneOfSubcategories => oneOfSubcategories.id === parseInt(product.subcategory))[0];
	};
	
	return (
		<ol className="breadcrumb">
			<li className="breadcrumb-item lead">
				<Link href="/">Главная</Link>
			</li>
			<li className="breadcrumb-item lead">
				<Link href="/products/1">Товары</Link>
			</li>
				{( subcategory === undefined && category !== undefined ) ? (
					<li className="breadcrumb-item lead">
						<Link href={`/products/${category.id}/${page}`}>
							{category.name} - стр. {page}
						</Link>
					</li>
				)
				: (category !== undefined ) && (
					<li className="breadcrumb-item lead">
						<Link href={`/products/${category.id}/1`} >
							{category.name}
						</Link>
					</li>
				)
			}
			{( product === undefined && (category !== undefined && subcategory !== undefined) ) ? (
				<li className="breadcrumb-item lead">
					<Link href={`/products/${category.id}/${subcategory.id}/${page}`} >
						{subcategory.name} - стр. {page}
					</Link>
				</li>
			)
			: ( product !== undefined ) && (
				<li className="breadcrumb-item lead">
					<Link href={`/products/${category.id}/${subcategory.id}/1`} >
						{subcategory.name}
					</Link>
				</li>
			)
			}
			{(searchQuery !== undefined) && (
				<li className="breadcrumb-item lead">
					<Link href={`/products/?search_query=${searchQuery}`}>
						Поиск - {searchQuery}
					</Link>
				</li>
			)}
			{(product !== undefined) && (
				<li className="breadcrumb-item lead">
					<Link href={`/product/${product.id}`}>
						{product.name}
					</Link>
				</li>
			)}
		</ol>
	);
};

export default Breadcrumbs;