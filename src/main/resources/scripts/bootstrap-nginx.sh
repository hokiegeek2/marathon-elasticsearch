#!/bin/bash

#Set passwords for nginx.conf file
htpasswd -c -b /etc/nginx/.htpasswd $USERNAME $PASSWORD

#Generate nginx.conf file
python -c 'from marathon.nginx import nginx_resource_management; nginx_resource_management.writeConfFile()'

#Generate initial ES nodes string used for comparison in health check and set env variable
export ES_NODES=$(python -c 'from marathon.nginx import nginx_resource_management; nodes = nginx_resource_management.getESNodes(); print(nodes.sort().str())')

echo "configuration file written, launching nginx"
nginx -g "daemon off;"
