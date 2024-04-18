#!/usr/bin/sh

# Create a temporary directory
temp_dir=$(mktemp -d)

mkdir -p /workspace/kaesluder.github.io/bin 


# Download a tar file into the temporary directory
wget -P "$temp_dir" https://github.com/gohugoio/hugo/releases/download/v0.125.0/hugo_extended_0.125.0_Linux-64bit.tar.gz
# Extract the contents of the tar file into a specific folder
tar -xvf "$temp_dir/hugo_extended_0.125.0_Linux-64bit.tar.gz" -C /workspace/kaesluder.github.io/bin 

# Download a tar file into the temporary directory
wget -P "$temp_dir" https://github.com/helix-editor/helix/releases/download/24.03/helix-24.03-x86_64-linux.tar.xz 
# Extract the contents of the tar file into a specific folder
tar -xvf "$temp_dir/helix-24.03-x86_64-linux.tar.xz" --strip-components=1 -C /workspace/kaesluder.github.io/bin 

# Download a tar file into the temporary directory
wget -P "$temp_dir" https://github.com/zellij-org/zellij/releases/download/v0.40.0/zellij-x86_64-unknown-linux-musl.tar.gz
# Extract the contents of the tar file into a specific folder
tar -xvf "$temp_dir/zellij-x86_64-unknown-linux-musl.tar.gz" -C /workspace/kaesluder.github.io/bin 

# Remove the temporary directory
rm -r "$temp_dir"

sudo apt install -y hunspell ksh

# update theme submodules
git submodule update --init --recursive

export PATH=$PATH:/workspace/kaesluder.github.io/bin
