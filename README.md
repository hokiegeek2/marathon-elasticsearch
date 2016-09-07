# marathon-elasticsearch 

This is a framework based upon the outstanding work of Chris Kite @ https://github.com/chriskite/elasticsearch-marathon. This framework features deployment of an Elasticsearch cluster on Marathon, using a bootstrap script approach for service discovery of all ES nodes within a cluster.

#Addition Features
I've converted all service discovery logic to Python and added a few more elements:

1. Option for Bridge or Host networking
2. Extension of service discovery to enable clustering across Marathon applications and application groups
3. Load balancing and single-host proxy with nginx

#marathon-elasticsearch image configuration

Environment

MARATHON_URL=http://<dns name or ip address of Marathon host>:8080
APP_NAME=tab-delimited list of Marathon application names
NETWORK_MODE=HOST or BRIDGE

Parameters
volume=mapping of host directory to container directory

#marathon-es-cluster-nginx configuration

Environment

MARATHON_URL=http://<dns name or ip address of Marathon host>:8080
APP_NAME=tab-delimited list of Marathon application names