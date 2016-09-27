#!/bin/bash

#Generate nginx url kibana will connect to
nginx_url=$(python -c 'from marathon.nginx import nginx_resource_management; \
     host = nginx_resource_management.getNginxHost(); print(host)')

#Set initial nginx host
python -c 'from marathon.nginx import nginx_resource_management; nginx_resource_management.writeInitialNginxHostString("/tmp/nginx_host.txt")'
     
#Start kibana
/opt/kibana/bin/kibana --elasticsearch.url=$nginx_url
