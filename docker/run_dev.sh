#!/bin/bash
xhost +

docker run --rm -ti \
    --name tdv_scraper \
    -v $PWD/:/app/ \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -p 8888:8888 \
    tdv_scraper:latest \
    ./scripts/jn.sh
    # ./scripts/start.sh 
    # bash

# docker exec -ti tdv_scraper bash;