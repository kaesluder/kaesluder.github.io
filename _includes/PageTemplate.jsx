import HeaderComponent from "../_components/HeaderComponent.jsx";
import TopMenu from "../_components/TopMenu.jsx";

export default (PageData, _helpers) => {
  const headerData = PageData;
  return (
    <html>
      <HeaderComponent {...headerData} />
      <body className="prose prose-invert bg-stone-950 container mx-auto">
        <div className="flex flex-col items-center">
          <TopMenu />
          <main className="bg-stone-900 p-3 rounded">{PageData.children}</main>
        </div>
      </body>
    </html>
  );
};
