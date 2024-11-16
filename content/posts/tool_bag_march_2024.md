+++
title = 'Tool Bag, March 2024'
date = 2024-03-20
draft = false
+++

This is just a grab-bag of tools that I'm using this month. I'm a bit of a command-line native, and lately been managing the tradeoff between features and focus. More buttons and menus creates more distractions *for me.* 

### OpenSUSE Tumbleweed with KDE (operating system)

One of the advantages (or disadvantages depending on your perspective) is having dozens of choices in both core system and user interface. Every one in the business has their own ideas about which customers to reach, and how to design for them. Ubuntu has their own ideas about how to make things "easy" for users. And that's not been working for me lately.

[OpenSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/) strikes a fair balance between stability and software availability not dependent on Snaps. Package updates are evaluating through an automated quality-testing platform. And honestly, it's the first time in a long time when everything just works.

Desktop choices are largely a personal decision. Somehow I always end up in KDE eventually. In the past, working with audio and locking on sleep have been significant blockers. 

### Helix (text editor)

Every few years, I go on a sidequest to find the perfect editor for me. Usually, I end up in emacs or vim. The last few years, it has been VSCode because it was used at Ada Developers Academy. I've dipped my toes into the water with emacs and vim (more properly neovim) and been put off by plugins, configs, and opinionated "starter kits."

A big selling point for helix is Language Server Protocol (LSP) integration built into the editor from the start with no or minimal config. This includes:

* syntax highlighting
* auto formatting
* pop-up code documentation and hints
* basic syntax checking
* navigation and selection for named code blocks (like functions)

Helix is a terminal-friendly modal editor like vim that uses a different model for selecting and modifying text. The select-act model gives me a chance to review the modified text before committing the modification. The [helix web site](https://helix-editor.com) does a better job of explaining the differences. (One infrequently-cited difference: copy/paste to system clipboard is one of those things I end up needing to configure in vim and emacs.)

At least for me, I find terminal editors cozy.

### Podman (container runner)

Most of my gig work is checking the accuracy of Python data-analysis scripts. I use [Jupyter Lab](https://jupyter.org) in a sandbox, and [Podman](https://podman.io) can run docker containers without needing a system daemon. My full command for launching Podman is:

```bash
podman run -it --rm -p 8888:8888 \
  -v "${PWD}":/home/jovyan/work:rw,z \
  -v ${HOME}/Downloads:/home/jovyan/downloads:ro,z \
  quay.io/jupyter/scipy-notebook:latest
```

This gives me a short-term Jupyter environment with read-only access to data files in Downloads. 

test
