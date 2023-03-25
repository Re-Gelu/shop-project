import { useRouter } from 'next/router';
import Link from 'next/link';

const Breadcrumbs = (props) => {
	const { categories, subcategories } = {...props};
	const router = useRouter();

	let category = undefined;
	let subcategory = undefined;
	let page = undefined;
	let searchQuery = undefined;

	const slug = router.query.slug;

	if (slug.length === 3) {
		subcategory = slug[1];
		page = slug[2];
    } else if (slug.length === 2) {
		subcategory = slug[0];
		page = slug[1];
    } else if (slug.length === 1) {
		page = slug[0];
    }

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
				: (category) && (
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