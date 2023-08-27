#!/bin/bash
xhost +

docker run --rm -ti \
    --name tdv_scraper \
    -v $PWD/:/app/ \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    tdv_scraper:latest
    # ./scripts/start.sh 
    # bash

# docker exec -ti tdv_scraper bash;