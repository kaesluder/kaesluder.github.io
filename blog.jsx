import { FaLinux } from "react-icons/fa";
import { FaReact } from "react-icons/fa";
import { FaJs } from "react-icons/fa";


export const layout = "./_includes/PageTemplate.jsx";
export const title = "Blog Index";



const iconList = (icons) => {
  return icons.map((icon) => {
    switch (icon) {
      case "linux":
        return <FaLinux key="linux" alt="linux" className="size-8" />;
      case "react":
        return <FaReact key="react" alt="react" className="size-8" />;
      case "javascript":
        return <FaJs key={icon} alt={icon} className="size-8" />;
      default:
        return null; // Return null or some default JSX if the icon is not recognized
    }
  });
};

export default function (data) {
  const posts = data.search.pages("type=post");
  posts.sort((a, b) => (a.date < b.date ? 1 : -1));
  return (
    <section>
      {posts.map((post) => {
        return (
          <a 
            key={post.url}
            href={post.url}
            className="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700 mb-3"
          >
            <figure className="w-20 grid grid-cols-2 gap-2 m-2">
          {post.icons ? iconList(post.icons) : ""}
            </figure>
            <div className="flex flex-col justify-between p-4 leading-normal">
              <h5 className="mb-0 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                {post.title}
              </h5>
              <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">
                {post.date.toLocaleDateString()}
              </p>
            </div>
          </a>
        );
      })}
    </section>
  );
}
