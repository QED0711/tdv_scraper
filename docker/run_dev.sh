#!/bin/bash
xhost +

docker run --rm -ti -d \
    --name tdv_scraper \
    -v $PWD/:/home/user/app \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    tdv_scraper:latest
    # bash
    # ./scripts/start.sh 

# docker exec -ti tdv_scraper bash;