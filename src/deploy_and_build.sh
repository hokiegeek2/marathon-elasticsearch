#!/bin/bash

sudo docker build -t hokiegeek2/marathon-elasticsearch -f Dockerfiles/marathon-elasticsearch .
sudo docker push hokiegeek2/marathon-elasticsearch

