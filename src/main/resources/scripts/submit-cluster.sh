#!/bin/bash

echo "Submitting ES Cluster"
curl --silent -XPOST $1?force=true -T $2 -H "Content-type: application/json"
echo "Submitted ES Cluster"
