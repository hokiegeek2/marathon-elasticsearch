#!/bin/bash
nodes=$(python -c 'from marathon.elasticsearch import resource_management; nodes = resource_management.getMarathonESNodes(); print(es_nodes)')

