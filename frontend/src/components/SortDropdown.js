const SortDropdown = (props) => {
  return (
		<div className="float-end">
		<button className="btn btn-secondary dropdown-toggle m-0 me-1" type="button" aria-haspopup="true">
			Сортировка
		</button>
		<div className="p-0 rounded uk-drop uk-dropdown" uk-dropdown="pos: bottom-center">
			<form className="list-group rounded" method="GET">
				<input
					type="submit"
					className="btn-check"
					name="sort_by"
					id="btnradio1"
					autoComplete="off"
					value="1"
				/>
				<label className="list-group-item list-group-item-action btn-outline-primary rounded-top" htmlFor="btnradio1">
					Новинки
				</label>
				<input
					type="submit"
					className="btn-check"
					name="sort_by"
					id="btnradio2"
					autoComplete="off"
					value="2"
				/>
				<label className="list-group-item list-group-item-action btn-outline-primary" htmlFor="btnradio2">
					Сначала дешёвые
				</label>
				<input
					type="submit"
					className="btn-check"
					name="sort_by"
					id="btnradio3"
					autoComplete="off"
					value="3"
				/>
				<label className="list-group-item list-group-item-action btn-outline-primary" htmlFor="btnradio3">
					Сначала дорогие
				</label>
				<input
					type="submit"
					className="btn-check"
					name="sort_by"
					id="btnradio4"
					autoComplete="off"
					value="4"
				/>
				<label className="list-group-item list-group-item-action btn-outline-primary rounded-bottom" htmlFor="btnradio4">
					По размеру скидки
				</label>
			</form>
		</div>
		</div>
  	);
};

export default SortDropdown;