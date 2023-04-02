import Link from 'next/link';

const Header = (props) => {
    return (
        /* <!-- Header --> */
        <header id="header" className="navbar navbar-expand-xl sticky-top">    
            <div className="container-fluid">

                {/* <!-- Left header block - Logo --> */}
                <Link href="/" className="navbar-brand logo ms-3">SITE_NAME</Link>

                {/* <!-- Navbar toggler --> */}
                <button type="button" className="navbar-toggler text-black" data-bs-toggle="collapse"
                data-bs-target="#navbar-menu" aria-controls="navbar-menu" 
                aria-expanded="false" aria-label="Переключатель навигации">
                    <i className="bi bi-list"></i>
                </button>

                {/* <!-- Navigation menu --> */}
                <nav id="navbar-menu" className="navbar-collapse collapse">

                    <hr className="d-xl-none border-top-colored" /> 

                    <ul className="navbar-nav top-nav-menu me-auto d-inline-flex">
                        <li className="nav-item px-4">
                            <Link className="nav-link text-reset uk-button-text" aria-current="page" href="/">Домой</Link>
                        </li>

                        <li className="nav-item px-4">
                            <Link className="nav-link text-reset uk-button-text " href="/contacts">Контакты</Link>
                        </li>

                        <li className="nav-item px-4">
                            <Link className="nav-link text-reset uk-button-text " href="/delivery">Доставка</Link>
                        </li>

                        <li className="nav-item px-4">
                            <Link className="nav-link text-reset uk-button-text " href="/about">О нас</Link>
                        </li>
                
                    </ul>

                    <hr className="d-xl-none border-top-colored" /> 

                    {/* <!-- Right header block --> */} 
                    <div className="d-inline-flex">
                        <div className="header-element me-5 ms-3 a-important" tabIndex="0" aria-haspopup="true"><i className="bi bi-search fs-2"></i></div>

                        {/* <!-- Search form --> */} 
                        <div className="uk-navbar-dropdown uk-drop" uk-drop="mode: click; cls-drop: uk-navbar-dropdown; boundary: !nav">
                            <div className="uk-grid-small uk-flex-middle uk-grid uk-grid-stack" uk-grid="true">
                                <div className="uk-width-expand">
                                    <div className="uk-search uk-search-navbar uk-width-1-1"> {/* method="get" action="{% url 'products' %}" */}
                                        <input className="uk-search-input" name="search_query" id="search_query" type="search" placeholder="Поиск..."  autoComplete="off" autoFocus />
                                    </div>
                                </div>
                                <div className="uk-width-auto">
                                    <div className="a-important uk-navbar-dropdown-toggle" uk-toggle="target: .uk-navbar-dropdown" tabIndex="0"><i className="bi bi-x-lg fs-4"></i></div>
                                </div>
                            </div>
                        </div>

                        <Link className="header-element me-5" href="/dashboard">
                            <i className="bi bi-person fs-1"></i>
                        </Link>

                        <div id="shopping-cart-offcanvas-open-button" className="header-element me-5 a-important" href="#shopping-cart-offcanvas" data-bs-toggle="offcanvas" aria-controls="shopping-cart-offcanvas">
                            <i className="bi bi-cart2"></i>
                        </div>

                    </div>

                </nav>
            </div>
        </header>
        
    );
};

export default Header;