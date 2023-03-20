import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import React from "react"
import MainLayout2 from '@/components/MainLayout2.js';
import ProductCard from "@/components/ProductCard.js";
import axios from '@/api.js';

const inter = Inter({ subsets: ['latin'] })

const IndexPage = (props) => {
	const {
		categories,
		subcategories,
		index} = {...props};

	return (
		<MainLayout2 {...{categories, subcategories}}>
			{index.map(category =>
                <section className="row mt-3 g-0" key={category.id}>

                    <div className="uk-card border p-3">
                        
                        <div>
                            <a href={`/products/${category.name}`} className="row my-2 ms-2 lead text-colored d-inline-block"><i className="bi bi-caret-right"></i>{category.name}</a>
                            <hr className="border-top-colored"/>

                            <div className="row uk-position-relative uk-visible-toggle px-3" tabIndex="-1" uk-slider="sets: true, finite: true, draggable: true">
                                
                                <ul className="uk-slider-items uk-child-width-1-1 uk-child-width-1-2@s uk-child-width-1-3@m uk-child-width-1-4@l" style={{"maxHeight    ": 100 + "%"}}>

                                    <li id="scroller-item" className="card me-4 overflow-auto" tabIndex="0">
                                            <div className="card-header">
                                                <div className="lead text-colored">Подкатегории: </div>
                                            </div>

                                            <div className="card-body">
                                               {category.subcategories.map((subcategory, key) => {
                                                    if (subcategory.category === category.id) {
                                                        return (
                                                            <React.Fragment key={subcategory.id}>
                                                                <p className="my-3">
                                                                    <a href={`/products/${category.name}/${subcategory.name}`} className="uk-button-text my-2 a-important">
                                                                        {subcategory.name}
                                                                    </a>
                                                                </p>
                                                                {key !== category.subcategories.length - 1 && 
                                                                    <hr className="text-black-50" />
                                                                }
                                                            </React.Fragment>
                                                        );
                                                    }
                                                    return null;
                                                })}
                                            </div>
                                    </li>

                                    {category.products.map((product) => (
                                        <li id="scroller-item" className="me-3" key={product.id}>
                                            <ProductCard product={product} cardAnimationClass="uk-transition-slide-left-small" />
                                        </li>
                                    ))}

                                    {category.products.length > 0 && (
                                        <li className="uk-transition-toggle me-3">
                                            <div className="h-100 card uk-card-hover uk-transition-opaque uk-transition-slide-left-small py-5">
                                                <a className="card-body lead fs-3 text-colored my-5 py-5 text-center" href={`/products/${category.name}`}>
                                                    Больше товаров...
                                                </a>
                                            </div>
                                        </li>
                                    )}

                                </ul>
                            </div>
                            
                        </div>
                    </div>

                </section>
            )}
		</MainLayout2>
	)
};

export async function getStaticProps() {
	const categoriesResponse = await axios.get('categories');
	const subcategoriesResponse = await axios.get('subcategories');
	const indexResponse = await axios.get('index_page');
	const categories = categoriesResponse.data;
	const subcategories = subcategoriesResponse.data;
	const index = indexResponse.data;
	return {
		props: {
			categories,
			subcategories,
			index
		}
	}
};

export default IndexPage;

{/* <>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <div className={styles.description}>
          <p>
            Get started by editing&nbsp;
            <code className={styles.code}>src/pages/index.js</code>
          </p>
          <div>
            <a
              href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
              target="_blank"
              rel="noopener noreferrer"
            >
              By{' '}
              <Image
                src="/vercel.svg"
                alt="Vercel Logo"
                className={styles.vercelLogo}
                width={100}
                height={24}
                priority
              />
            </a>
          </div>
        </div>

        <div className={styles.center}>
          <Image
            className={styles.logo}
            src="/next.svg"
            alt="Next.js Logo"
            width={180}
            height={37}
            priority
          />
          <div className={styles.thirteen}>
            <Image
              src="/thirteen.svg"
              alt="13"
              width={40}
              height={31}
              priority
            />
          </div>
        </div>

        <div className={styles.grid}>
          <a
            href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Docs <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Find in-depth information about Next.js features and&nbsp;API.
            </p>
          </a>

          <a
            href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Learn <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Learn about Next.js in an interactive course with&nbsp;quizzes!
            </p>
          </a>

          <a
            href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Templates <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Discover and deploy boilerplate example Next.js&nbsp;projects.
            </p>
          </a>

          <a
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Deploy <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Instantly deploy your Next.js site to a shareable URL
              with&nbsp;Vercel.
            </p>
          </a>
        </div>
      </main>
    </> */}