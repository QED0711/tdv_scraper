#!/bin/bash
xhost +

docker run --rm -ti -d \
    --name tdv_scraper \
    -v $PWD/:/app/ \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=$DISPLAY \
    -e HEADLESS_SELENIUM=true \
    -p 8888:8888 \
    -p 8000:8000 \
    tdv_scraper:latest
