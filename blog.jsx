export default function (data) {
  const posts = data.search.pages("type=post");
  posts.sort((a, b) => (a.date < b.date ? 1 : -1));
  return (
    <section>
      {posts.map((post) => {
        return (
          <li key={post.url}>
            <a href={post.url}>
              {post.title}
            </a>
            {post.date.toLocaleDateString()}
          </li>
        );
      })}
    </section>
  );
}
