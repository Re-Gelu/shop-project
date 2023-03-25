import Breadcrumbs from "@/components/Breadcrumbs.js";
import SortDropdown from "@/components/SortDropdown.js";

const TopRow = (props)=> {
	return (
		<div className="row mb-1 mx-0 px-0">
			<nav className="col-10" aria-label="breadcrumb">
				<Breadcrumbs {...props} />
			</nav>
			<div className="col-2 pe-0">
				{props.products && <SortDropdown />}
			</div>
		</div>
	);
};

export default TopRow;