import { FaLinkedin, FaGithub } from "react-icons/fa";

export default () => {
  return (
    <footer className="mt-3 flex flex-col items-center">
      <ul className="inline-flex space-x-3 m-1 list-none">
        <li>
          <a
            href="https://www.linkedin.com/in/kae-sluder/"
            className="flex item-center mr-2"
          >
            <FaLinkedin className="size-6" />
            LinkedIn
          </a>
        </li>
        <li>
          <a
            href="https://github.com/kaesluder"
            className="flex item-center mr-2"
          >
            <FaGithub className="size-6" />
            Github
          </a>
        </li>
      </ul>
    <p className="mt-0">&copy; 2024 Kae Job Sluder, Creative Commons BY 4.0</p>
    </footer>
  );
};
