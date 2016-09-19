#!/bin/bash

es_url=$(python -c 'from marathon.nginx import nginx_resource_management; \
     host = nginx_resource_management.getNginxHost(); print(host)')

/opt/kibana/bin/kibana --elasticsearch.url=$es_url
