import { useRouter } from 'next/router';
import Link from 'next/link';

const Breadcrumbs = (props) => {
	const { categories, subcategories } = {...props};
	const router = useRouter();
	let { category, subcategory, page, searchQuery } = router.query;
	category = categories.filter(oneOfCategories => oneOfCategories.id === parseInt(category))[0];
	subcategory = subcategories.filter(oneOfSubcategories => oneOfSubcategories.id === parseInt(subcategory))[0];

	return (
		<ol className="breadcrumb">
			<li className="breadcrumb-item lead">
				<Link href="/">Главная</Link>
			</li>
			<li className="breadcrumb-item lead">
				<Link href={`products/`}>Товары</Link>
			</li>
				{(category & !subcategory) ? (
					<li className="breadcrumb-item lead">
						<Link href={`products/${category.id}/${page}`}>
							{...category.name} - стр. {page}
						</Link>
					</li>
				)
				:
				(
					<li className="breadcrumb-item lead">
						<Link href={`/products/${category.id}/1`} >
							{category.name}
						</Link>
					</li>
				)
			}
			{(category && subcategory ) && (
				<li className="breadcrumb-item lead">
					<Link href={`/products/${category.id}/${subcategory.id}/${page}`} >
						{subcategory.name} - стр. {page}
					</Link>
				</li>
			)}
			{searchQuery && (
				<li className="breadcrumb-item lead">
					<Link href={`products/?search_query=${searchQuery}`}>
						Поиск - {searchQuery}
					</Link>
				</li>
			)}
		</ol>
	);
};

export default Breadcrumbs;