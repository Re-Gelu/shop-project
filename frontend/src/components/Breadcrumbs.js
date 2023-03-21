function Breadcrumbs({ category, subcategory, searchQuery }) {
  return (
    <ol className="breadcrumb">
      <li className="breadcrumb-item lead">
        <Link to="/">Главная</Link>
      </li>
      <li className="breadcrumb-item lead">
        <Link to={{ pathname: "/products", search: "?page=1" }}>Товары</Link>
      </li>
      {category && (
        <li className="breadcrumb-item lead">
          <Link
            to={{ pathname: "/products", search: "?page=1", state: { category } }}
          >
            {category}
          </Link>
        </li>
      )}
      {subcategory && (
        <li className="breadcrumb-item lead">
          <Link
            to={{
              pathname: "/products",
              search: "?page=1",
              state: { category, subcategory },
            }}
          >
            {subcategory}
          </Link>
        </li>
      )}
      {searchQuery && (
        <li className="breadcrumb-item lead">
          <Link
            to={{
              pathname: "/products",
              search: `?search_query=${searchQuery}`,
            }}
          >
            Поиск - {searchQuery}
          </Link>
        </li>
      )}
    </ol>
  );
}