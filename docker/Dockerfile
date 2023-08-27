FROM ubuntu:22.04
ENV TZ="America/New_York"

# container setup
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
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


RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user/app

COPY ./config/requirements.txt /home/user/app
RUN pip install -r requirements.txt

COPY ./scripts /home/user/app

ENV DISPLAY=:99

CMD ["./scripts/start.sh"]