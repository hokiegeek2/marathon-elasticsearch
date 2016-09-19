i#!/bin/bash

htpasswd -c -b /etc/nginx/.htpasswd $USERNAME $PASSWORD

python -c 'from marathon.nginx import nginx_resource_management; nginx_resource_management.writeConfFile()'
echo "configuration file written, launching nginx"
nginx -g "daemon off;"
