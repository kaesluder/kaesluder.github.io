export default ({ title, description, keywords }) => {
  return (
    <head>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="keywords" content={keywords} />
      <meta name="author" content="Kae Job Sluder" />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:type" content="article" />
      <link rel="stylesheet" href="/styles.css" />
    </head>
  );
};
