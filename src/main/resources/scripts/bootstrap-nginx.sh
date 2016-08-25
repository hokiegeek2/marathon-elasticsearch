#!/bin/bash
python -c 'from marathon.nginx import nginx_resource_management; nginx_resource_management.writeConfFile()'

exec nginx -g daemon off