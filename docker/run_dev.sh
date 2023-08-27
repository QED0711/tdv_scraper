#!/bin/bash

docker run --rm -ti -d \
    --name tdv_scraper \
    tdv_scraper:latest \
    bash;

docker exec -ti tdv_scraper bash;