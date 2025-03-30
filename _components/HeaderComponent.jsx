export default ({ title, description }) => {
  return (
    <head>
 <link href=" https://cdn.jsdelivr.net/npm/highlightjs-themes@1.0.0/tomorrow-night-blue.min.css " rel="stylesheet" />     
    <title>{title}</title>
      <meta name="description" content={description ? description : "Kae Job Sluder: Home page and blog."} /> 
      <meta name="author" content="Kae Job Sluder" />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description ? description : "Kae Job Sluder: Home page and blog."} />
      <meta property="og:type" content="article" />
      <link rel="stylesheet" href="/styles.css" />
    </head>
  );
};
