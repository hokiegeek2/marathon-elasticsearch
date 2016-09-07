#!/bin/bash

host=$(python -c 'from marathon.elasticsearch import nginx_resource_management; nginx_resource_management.getNginxHost; \
     host = resource_management.getHost(); print(host)')
     
export NGINX_HOST=host

echo $NGINX_HOST