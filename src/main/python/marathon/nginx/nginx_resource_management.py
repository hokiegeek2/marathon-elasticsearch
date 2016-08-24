import os
from marathon.elasticsearch import resource_management

def writeConfFile():
    nodes = getESNodes()
    port = os.getenv("PORT0")
    file_path = os.getenv("CONF_FILE")
    
    with open(file_path, "wt") as fout:
        fout.write("upstream elasticsearch_servers { \n")
        fout.write("\t  zone elasticsearch_servers 64K; \n")
        for node in nodes:
            fout.write("\t " + node + ";")
        fout.write("}")
        fout.write("\n")
        fout.write("\t server { \n")
        fout.write("\t \t listen: " + port + ";")
        fout.write("\n")
        fout.write("\t \t location / { \n")
        fout.write("\t \t proxy_pass http://elasticsearch_servers; \n")
        fout.write("\t \t proxy_http_version 1.1; \n")
        fout.write("\t } \n")
        fout.write("\n")
        fout.write("\t  # redirect server error pages to the static page /50x.html \n")
        fout.write("\t  error_page 500 502 503 504 /50x.html; \n")
        fout.write("\t  location = /50x.html { \n")
        fout.write("\t \t   root /usr/share/nginx/html; \n")
        fout.write("\t } \n")
        fout.write("} \n")
        fout.close()
        
def getESNodes():
    return resource_management.getMarathonESNodes()