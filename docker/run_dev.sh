#!/bin/bash
xhost +
# export DISPLAY=:0

docker run --rm -ti \
    --name tdv_scraper \
    -v $PWD/:/app/ \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -p 8888:8888 \
    -p 8000:8000 \
    tdv_scraper:latest bash

    # ./scripts/jn.sh
    # ./scripts/start.sh 
    # bash

# docker exec -ti tdv_scraper bash;