#!/bin/bash
hosts=$(python -c 'import os; from marathon.elasticsearch import resource_management; hosts = resource_management.getMarathonAppHosts(os.getenv("MARATHON_URL") + "/v2/apps/" + os.getenv("APP_NAME")); print(hosts)')

host_name=$(python -c 'import os; from marathon.elasticsearch import resource_management; host = resource_management.getHost(os.getenv("HOSTNAME"), os.getenv("PORT1")); print(host)')

host=$(python -c 'import os; host = str(os.getenv("HOST")).split(".")[0].strip("ip-").replace("-","."); print(host)')

echo $hosts
echo $host_name
exec /deploy/elasticsearch-2.3.5/bin/elasticsearch \
--node.name=$host \
--cluster.name=hokiegeek2 \
--network.bind_host=0.0.0.0 \
--network.publish_host=$host \
--discovery.zen.minimum_master_nodes=1 \
--discovery.zen.ping.multicast.enabled=false \
--discovery.zen.ping.unicast.hosts=$hosts \
--discovery.zen.ping_timeout=90s \
--discovery.zen.join_timeout=300s \
--discovery.zen.publish_timeout=300s \
--http.port=$PORT0 \
--transport.tcp.port=$PORT1 \
--transport.publish_port=$PORT1
#--network.publish_host=$host_name \


