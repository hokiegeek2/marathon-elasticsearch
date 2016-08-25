#!/bin/bash

python -c 'from marathon.nginx import nginx_resource_management; nginx_resource_management.writeConfFile()'
echo "configuration file written, launching nginx"
nginx -g "daemon off;"
echo "launched nginx"
