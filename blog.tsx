export default function (data: Lume.Data, _: Lume.Helpers) {
  const posts = data.search.pages("type=post");
  posts.sort((a, b) => (a.date < b.date ? 1 : -1));
  return (
    <section>
      {posts.map((post) => {
        return (
          <li>
            <a key={post.url} href={post.url}>
              {post.title}
            </a>
            {post.date.toLocaleDateString()}
          </li>
        );
      })}
    </section>
  );
}
