import lume from "lume/mod.ts";
import jsx from "lume/plugins/jsx.ts";
import tailwindcss from "lume/plugins/tailwindcss.ts";
import postcss from "lume/plugins/postcss.ts";
import typography from "npm:@tailwindcss/typography";
import codeHighlight from "lume/plugins/code_highlight.ts";

const site = lume();

site.use(
  tailwindcss({
    options: {
      plugins: [typography],
    },
  }),
);
site.use(
  codeHighlight({
    theme: { name: "tomorrow-night-blue", cssFile: "/highlight.css" },
  }),
);
site.use(jsx(/* Options */));
site.use(postcss());
site.loadAssets([".css"]);
site.copyRemainingFiles(
  (path: string) => path.startsWith("/images/"),
);

export default site;
