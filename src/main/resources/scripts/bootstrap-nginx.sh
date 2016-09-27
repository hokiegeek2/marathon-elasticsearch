#!/bin/bash

#Set passwords for nginx.conf file
htpasswd -c -b /etc/nginx/.htpasswd $USERNAME $PASSWORD

#Generate nginx.conf file
python -c 'from marathon.nginx import nginx_resource_management; nginx_resource_management.writeConfFile()'
echo "configuration file written, launching nginx"

#Generate initial ES nodes string used for comparison in health check
python -c 'from marathon.nginx import nginx_resource_management; nodes = nginx_resource_management.writeInitialESNodesString("/tmp/es_nodes.txt")'
echo "generated list of ES nodes and wrote out file, starting nginx"

#Start nginx
nginx -g "daemon off;"
