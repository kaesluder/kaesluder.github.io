import HeaderComponent from "../_components/HeaderComponent.jsx";
import TopMenu from "../_components/TopMenu.jsx";
import Footer from "../_components/Footer.jsx";

export default (PageData, _helpers) => {
  const headerData = PageData;
  return (
    <html>
      <HeaderComponent {...headerData} />
      <body className="prose prose-invert bg-stone-950 container mx-auto ">
        <div className="flex flex-col items-center">
          <TopMenu />
          <h1>{PageData.title}</h1>
          <main className="bg-stone-900 p-3 rounded w-100">
            {PageData.children}
          </main>
          <Footer />
        </div>
      </body>
    </html>
  );
};
