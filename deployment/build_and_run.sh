#!/usr/bin/env bash

docker build --tag drf .
docker run -p 5010:8000
    --restart always
    --name drf_container drf > logs.txt 2>&1 &
