FROM python:3.8-buster
ENV TZ="America/New_York"

# container setup
RUN apt-get update && apt-get install -y \
    jupyter-core \
    jupyter-notebook \
    vim \
    nano \
    tmux \
    chromium

# Chromium setup for salenium
WORKDIR /usr/bin
RUN wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip


WORKDIR /app

COPY ./config/requirements.txt /app
RUN pip install -r requirements.txt



