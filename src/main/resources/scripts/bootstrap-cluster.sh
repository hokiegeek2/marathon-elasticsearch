#!/bin/bash
hosts=$(python -c 'from marathon.elasticsearch import resource_management; hosts = resource_management.getMarathonAppHosts(); print(hosts)')
host=$(python -c 'from marathon.elasticsearch import resource_management; host = resource_management.getHost(); print(host)')
transport_port=$(python -c 'from marathon.elasticsearch import resource_management; tp = resource_management.getTransportBindPort(); print(tp)')
node_name=$(python -c 'from marathon.elasticsearch import resource_management; tp = resource_management.getNodeName(); print(tp)')

exec /deploy/elasticsearch-2.3.5/bin/elasticsearch \
--node.name=$node_name \
--cluster.name=hokiegeek2 \
--network.bind_host=0.0.0.0 \
--network.publish_host=$host \
--discovery.zen.minimum_master_nodes=1 \
--discovery.zen.ping.multicast.enabled=false \
--discovery.zen.ping.unicast.hosts=$hosts \
--discovery.zen.ping_timeout=90s \
--discovery.zen.join_timeout=300s \
--discovery.zen.publish_timeout=300s \
--http.port=9200 \
--transport.tcp.port=$transport_port \
--transport.publish_port=$PORT1