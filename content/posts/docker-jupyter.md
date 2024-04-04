+++
title = 'Ephemeral Jupyter Container with JavaScript, Typescript, and Rust'
date = 2024-04-03
draft = false
+++

I must admit, I'm a bit of a latecomer to containers and Jupyter. But my current gig involves testing a lot of AI-generated code. I somehow managed to break my last Jupyter Lab venv and had to start over, and realized that a container with a fixed spec would save a little bit of time. Each day, I can start with a (mostly) fresh environment without any library conflicts. Some of the requirements included:

- quick setup and teardown
- pre-install languages and libraries that I use frequently
- no messing with system-level files
- access to downloaded data files

## 1: Podman

I've run Docker before, I've also set up my own mail server before. I'm trying to simplify my life and wanted these containers to be fast and disposable. I also wanted to keep everything in my userspace as much as possible. [Podman](https://podman.io) is a container-runner that fits those requirements. The container starts up; the container shuts down, all without messing with groups or sudo. 

## 2: Jupyter Base Image

I used the [Jupyter scipy-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html) as a starting point. 
It has almost everything I want in this sandbox, so I can just focus on the few things I need to add. 

```Docker
# Use the Jupyter scipy notebook as a parent image
FROM quay.io/jupyter/scipy-notebook:latest

```

## 3: Global Config and Install as Root

Here I set up (most) of the rest of my system:

* fresh updates (from apt)
* nodejs (from apt)
* npm (from apt)
* [Evcxr Jupyter for Rust](https://github.com/evcxr/evcxr) (download and copy into path)
* [tslab](https://github.com/yunabe/tslab) (from node)

Evcxr and tslab both require an additional installation step to register with Jupyter. 

```Docker

# Use root to install additional packages
USER root

# Install any additional system packages required for your kernels here
# Example: RUN apt-get update && apt-get install -y package-name
# Install system dependencies
RUN apt-get update && apt-get install -y curl nodejs npm wget tar
# Install Rust and the EvCxR Jupyter kernel for Rust

# Download and extract the pre-built evcxr_jupyter binary
RUN wget https://github.com/evcxr/evcxr/releases/download/v0.17.0/evcxr_jupyter-v0.17.0-x86_64-unknown-linux-gnu.tar.gz -O evcxr_jupyter.tar.gz \
    && tar -xzf evcxr_jupyter.tar.gz -C /tmp \
    && mv /tmp/evcxr_jupyter-v0.17.0-x86_64-unknown-linux-gnu/evcxr_jupyter /usr/local/bin \
    && chmod +x /usr/local/bin/evcxr_jupyter

# Install the evcxr_jupyter kernel
RUN evcxr_jupyter --install

# Clean up
RUN rm evcxr_jupyter.tar.gz \
    && rm -r /tmp/evcxr_jupyter-v0.17.0-x86_64-unknown-linux-gnu

    
# Install iJavaScript for JavaScript and TypeScript
RUN npm install -g tslab \
    && tslab install --version \
    && tslab install

  
```

## 4: A Little Housecleaning

Jupyter runs under user jovyan in the Jupyter image I started with. These lines make sure that jovyan owns all of its own files.


```Docker
# make sure jovyan owns its files
# Create the 'jovyan' group if it doesn't already exist and add 'jovyan' user to it
RUN groupadd -f jovyan && usermod -aG jovyan jovyan &&  chown -R jovyan:jovyan /home/jovyan

# Switch back to jovyan to avoid running as root
USER jovyan
```

## 5: Install rustc and Some Optional Python Packages

Both of these probably could have been installed as root. Evxcr also requires rustc. I use the recommended rustup-as-user install to be consistent with my other rust installation. And pip complains (with good reason) about installing things at the system level instead of using a venv or distribution packages. 

```Docker
# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Update PATH for all subsequent instructions
ENV PATH="/home/jovyan/.cargo/bin:${PATH}"

RUN pip install tabulate
```

## 6: Wrap Up and Open a Port

Optionally copy some local files. Not so optionally, set up the port that will be forwarded to Jupyter. For convenience, this is the same port number used by Jupyter inside the container.

```Docker
# Copy files or directories from the host to the container
# COPY ./localpath /home/jovyan/work/localpath

# Expose the port Jupyter will run on
EXPOSE 8888

```

## 7: Build and Run

Finally, put the full Dockerfile into an empty directory. cd into the directory and run the build command.

```sh
podman build -t da-docker-image .
```

This will do all the magic including:

* downloading the base image
* installing software as root
* installing software as jovyan
* configuring the container to act as a Jupyter server.

Running the container is a simple shell command. 

```sh
podman run -it --rm -p 8888:8888 \
-v "${PWD}":/home/jovyan/work:rw,z \
-v ${HOME}/Downloads:/home/jovyan/downloads:ro,z \
da-docker-image
```

In order for this to work I had to set permissions to make the files visible to Jupyter:

```sh
chmod -r o+r ~/Downloads
chmod -r o+rw ~/scratch
```

The full Dockerfile is at the end of this post. 



```Docker
# Use the Jupyter scipy notebook as a parent image
FROM quay.io/jupyter/scipy-notebook:latest

# Use root to install additional packages
USER root

# Install any additional system packages required for your kernels here
# Example: RUN apt-get update && apt-get install -y package-name
# Install system dependencies
RUN apt-get update && apt-get install -y curl nodejs npm wget tar
# Install Rust and the EvCxR Jupyter kernel for Rust

# Download and extract the pre-built evcxr_jupyter binary
RUN wget https://github.com/evcxr/evcxr/releases/download/v0.17.0/evcxr_jupyter-v0.17.0-x86_64-unknown-linux-gnu.tar.gz -O evcxr_jupyter.tar.gz \
    && tar -xzf evcxr_jupyter.tar.gz -C /tmp \
    && mv /tmp/evcxr_jupyter-v0.17.0-x86_64-unknown-linux-gnu/evcxr_jupyter /usr/local/bin \
    && chmod +x /usr/local/bin/evcxr_jupyter

# Install the evcxr_jupyter kernel
RUN evcxr_jupyter --install

# Clean up
RUN rm evcxr_jupyter.tar.gz \
    && rm -r /tmp/evcxr_jupyter-v0.17.0-x86_64-unknown-linux-gnu

    
# Install iJavaScript for JavaScript and TypeScript
RUN npm install -g tslab \
    && tslab install --version \
    && tslab install


# make sure jovyan owns its files
# Create the 'jovyan' group if it doesn't already exist and add 'jovyan' user to it
RUN groupadd -f jovyan && usermod -aG jovyan jovyan &&  chown -R jovyan:jovyan /home/jovyan

# Switch back to jovyan to avoid running as root
USER jovyan

# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Update PATH for all subsequent instructions
ENV PATH="/home/jovyan/.cargo/bin:${PATH}"

RUN pip install tabulate


# Copy files or directories from the host to the container
# COPY ./localpath /home/jovyan/work/localpath

# Expose the port Jupyter will run on
EXPOSE 8888
```
