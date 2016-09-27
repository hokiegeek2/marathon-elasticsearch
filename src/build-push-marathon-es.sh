sudo docker build -t hokiegeek2/marathon-es-cluster-base -f Dockerfiles/marathon-es-cluster-base .
sudo docker build -t hokiegeek2/marathon-elasticsearch -f Dockerfiles/marathon-elasticsearch .
sudo docker build -t hokiegeek2/marathon-es-cluster-nginx -f Dockerfiles/marathon-es-cluster-nginx .
sudo docker build -t hokiegeek2/marathon-es-cluster-kibana -f Dockerfiles/marathon-es-cluster-kibana .
sudo docker push hokiegeek2/marathon-es-cluster-base
sudo docker push hokiegeek2/marathon-elasticsearch
sudo docker push hokiegeek2/marathon-es-cluster-nginx
sudo docker push hokiegeek2/marathon-es-cluster-kibana

