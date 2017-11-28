#!/bin/bash
hosts=$(python -c 'from marathon.elasticsearch import resource_management; hosts = resource_management.getMarathonAppHosts(); print(hosts)')
host=$(python -c 'from marathon.elasticsearch import resource_management; host = resource_management.getHost(); print(host)')
transport_port=$(python -c 'from marathon.elasticsearch import resource_management; tp = resource_management.getTransportBindPort(); print(tp)')
node_name=$(python -c 'from marathon.elasticsearch import resource_management; tp = resource_management.getNodeName(); print(tp)')
cluster_name=$(python -c 'from marathon.elasticsearch import resource_management; cluster = resource_management.getClusterName(); print(cluster)')
min_num_master_nodes=$(python -c 'from marathon.elasticsearch import resource_management; master_nodes = resource_management.getMinNumMasterNodes(); print(master_nodes)')
data_directories=$(python -c 'from marathon.elasticsearch import resource_management; data_dir = resource_management.getDataDirectories(); print(data_dir)')
node_type=$(python -c 'from marathon.elasticsearch import resource_management; nt = resource_management.getNodeType(); print (nt)')

exec /deploy/elasticsearch/bin/elasticsearch \
-Enode.name=$node_name \
-Ecluster.name=$cluster_name \
-Enetwork.bind_host=0.0.0.0 \
-Enetwork.publish_host=$host \
-Ediscovery.zen.minimum_master_nodes=$min_num_master_nodes \
-Ediscovery.zen.ping.unicast.hosts=$hosts \
-Ediscovery.zen.ping_timeout=90s \
-Ediscovery.zen.join_timeout=300s \
-Ediscovery.zen.publish_timeout=300s \
-Ehttp.port=9200 \
-Etransport.tcp.port=$transport_port \
-Etransport.publish_port=$PORT1 \
-Epath.data=$data_directories \
-Eaction.destructive_requires_name=true \
$node_type
