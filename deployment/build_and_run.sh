#!/usr/bin/env bash

docker build --tag drf .
docker run -p 5010:8000 --name drf_container drf > logs.txt 2>&1 &
