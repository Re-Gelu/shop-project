import { useRouter } from 'next/router';
import Link from 'next/link';

const Pagination = (props) => {
	const { currentPage, totalPages } = {...props};
	const router = useRouter();
    const {category, subcategory} = router.query;
	console.log(router.query);

	// Вычисляем диапазон страниц, которые нужно отобразить в пагинации
	const pageRange = [];
	for (let i = Math.max(currentPage - 2, 1); i <= Math.min(currentPage + 2, totalPages); i++) {
		pageRange.push(i);
	};

	// Генерируем элементы пагинации
	const paginationItems = [];

	// Кнопка "Previous"
	paginationItems.push(
		<li key="previous" className={`page-item${currentPage === 1 ? ' disabled' : ''}`}>
			<Link className="page-link text-colored" 
			href={{
				pathname: router.pathname,
				query: { 
					category: category,
					subcategory: subcategory,
					page: currentPage === 1 ? 1 : currentPage-1
				},
			}}>
			&laquo;
			</Link>
		</li>
	);

	// Элементы страниц
	for (let page of pageRange) {
		paginationItems.push(
			<li key={page} className={`page-item${currentPage === page ? ' active' : ''}`}>
				<Link className={`page-link${currentPage === page ? ' background-colored border-colored' : ' text-colored'}`} 
				href={{
					pathname: router.pathname,
					query: { 
						category: category,
						subcategory: subcategory,
						page: page
					},
				}}>
					{page}
				</Link>
			</li>
		);
	};

	// Элементы "..." для разделения длинных последовательностей страниц
	if (pageRange[0] > 1) {
		paginationItems.splice(1, 0,
			<li key="ellipsis-start" className="page-item">
				<span className="page-link text-colored">...</span>
			</li>
		);
	};
	if (pageRange[pageRange.length - 1] < totalPages) {
		paginationItems.splice(paginationItems.length - 1, 0,
			<li key="ellipsis-end" className="page-item">
				<span className="page-link text-colored">...</span>
			</li>
		);
	};

	// Кнопка "Next"
	paginationItems.push(
		<li key="next" className={`page-item${currentPage === totalPages ? ' disabled' : ''}`}>
			<Link className="page-link text-colored" 
			href={{
				pathname: router.pathname,
				query: { 
					category: category,
					subcategory: subcategory,
					page: currentPage === totalPages ? totalPages : currentPage+1
				},
			}}>
			&raquo;
			</Link>
		</li>
	);

	// Возвращаем сгенерированные элементы
	return (
		<nav>
			<ul className="pagination justify-content-center flex-wrap mt-3 mb-4 fs-4">
				{paginationItems}
			</ul>
		</nav>
	);
};

export default Pagination;