export default ({ title, children }: Lume.Data, _: Lume.Helpers) => (
  <html>
    <head>
      <title>{title}</title>
    </head>
    <body>
      {children}
    </body>
  </html>
);
