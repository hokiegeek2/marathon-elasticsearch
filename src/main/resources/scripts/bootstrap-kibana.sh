#!/bin/bash

es_url=$(python -c 'from marathon.elasticsearch import nginx_resource_management; nginx_resource_management.getNginxHost; \
     host = resource_management.getHost(); print(host)')
     
/opt/kibana/bin/kibana --elasticsearch.url=$es_url