# marathon-elasticsearch

This is a framework based upon the outstanding work of Chris Kite @ https://github.com/chriskite/elasticsearch-marathon. I've converted all service discovery logic to python and added a few more elements:

1. Option for Bridge or Host networking
2. Service discovery enables clustering across applications and application groups
3. Coming Soon--Kibana service discovery and explict assignment of Kibana instances to Elasticsearch nodes

Docker Environment Variables
MARATHON_URL=http://<dns name or ip address of Marathon host>:8080
APP_NAME=tab-delimited list of Marathon application names
NETWORK_MODE=HOST or BRIDGE

Docker Parameters
volume=mapping of host directory to container directory
