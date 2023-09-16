FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ="America/New_York"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# container setup
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    jupyter-core \
    jupyter-notebook \
    curl \
    wget \
    vim \
    nano \
    tmux \
    xvfb \
    x11-apps

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install Python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

WORKDIR /app

COPY ./config/requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

# Add a new group and user with specified UID and GID
RUN groupadd -g 1000 tdvgroup && \
    useradd -u 1000 -g tdvgroup -ms /bin/bash tdv

CMD ["./scripts/start.sh"]