const Preloader = (props)=> {
    return (
        <div className="container mt-3">
			<center className="col-md-12 text-center">
				<div className="p-5 m-5">
                    <div className="spinner-border text-secondary" 
                    style={{width: `${props.ratio}rem`, height: `${props.ratio}rem`}} role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                </div>
			</center>
		</div>
    );
};

Preloader.defaultProps = {
    ratio: 15
};

export default Preloader;