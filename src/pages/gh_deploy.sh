#!/usr/bin/env sh

pushd ../kaesluder.github.io
pwd
mkdocs gh-deploy --config-file ../kae-homepage-mkdocs/mkdocs.yml --remote-branch main 
popd