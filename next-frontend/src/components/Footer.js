const Footer = (props) => {
    return (
         /* <!-- Footer --> */
        <footer className="container text-center my-5">

            <div className="row justify-content-center h-100">
                <div className="col-5 my-auto p-0">
                    <hr className="text-black-50 my-0" />
                </div>

                <div className="col-auto my-auto">
                    <i className="bi bi-circle fs-4 opacity-25 my-0"></i>
                </div>

                <div className="col-5 my-auto p-0">
                    <hr className="text-black-50 my-0" />
                </div>	
            </div>

            <div className="mt-4">© 2022 Название сайта - Интернет-маркетплейс на Django</div>
            <sub className="text-colored float-end pt-4 pb-5 d-inline-flex">made by Re;Gelu
                <div className="waves-container mx-3">
                  <div className="wave" style={{"--i": 1}}></div>
                </div>
            </sub>
            
        </footer>
    );
};

export default Footer;