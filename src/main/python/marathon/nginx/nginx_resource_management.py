import os
from marathon.elasticsearch import resource_management

__all__ = '''
'''.split()

def writeConfFile():
    nodes = _getESNodes()
    port = os.getenv("PORT0")
    file_path = os.getenv("CONF_FILE")
    authenticate = os.getenv("AUTHENTICATE", False)
    with open(file_path, "wt") as fout:
        fout.write("events {\n")
        fout.write("\t worker_connections  1024;\n")
        fout.write("}\n")
        fout.write("http {\n")
        fout.write("\t upstream elasticsearch_servers { \n")
        for node in nodes:
            fout.write("\t\t server " + node + ";\n")
        fout.write("\t} \n")
        fout.write("\t server { \n")
        fout.write("\t\t listen " + port + ";\n")
        fout.write("\t\t location / { \n")
        
        if (authenticate):
            fout.write("\t\t auth_basic 'Enter Username and Password:'; \n")
            fout.write("\t\t auth_basic_user_file /etc/nginx/.htpasswd; \n")
            
        fout.write("\t\t client_max_body_size 1G; \n")
        fout.write("\t\t\t proxy_pass http://elasticsearch_servers; \n")
        fout.write("\t\t\t proxy_http_version 1.1; \n")
        fout.write("\t\t } \n")
        fout.write("\t\t  # redirect server error pages to the static page /50x.html \n")
        fout.write("\t\t  error_page 500 502 503 504 /50x.html; \n")
        fout.write("\t\t  location = /50x.html { \n")
        fout.write("\t\t\t root /usr/share/nginx/html; \n")
        fout.write("\t\t } \n")
        fout.write("\t } \n")
        fout.write("}")
        fout.close()

def writeInitialESNodesString(path):
    nodes = _getESNodes()
    nodes.sort();
    nodes_string = "".join(nodes)
    c_file = open(path,"w")
    c_file.write(nodes_string)
    c_file.close()

def writeInitialNginxHostString(path):
    host = _getNginxHost()
    h_file = open(path,"w")
    h_file.write(host)
    h_file.close()

def _getESNodes():
    return resource_management.getMarathonESNodes()

def _getNginxHost():
    nginx_name = os.getenv("NGINX_APP_NAME")
    nginx_url = resource_management.getAppURL(nginx_name)
    json_data = resource_management.getMarathonAppJSON(nginx_url)
    app_host = json_data["app"]["tasks"][0]
    host_string = "http://"
    host_string += getAuthInfo()
    host_string += app_host["host"]
    host_string += ":"
    host_string += str(app_host["ports"][0])
    return host_string

def generateHostString(app_host):
    host_string = "http://"
    host_string += getAuthInfo()
    host_string += app_host["host"]
    host_string += ":"
    host_string += str(app_host["ports"][0])

def getAuthInfo():
    user = os.getenv("USERNAME")
    pwd  = os.getenv("PASSWORD")
    if (pwd != None and user != None):
        return user + ":" + pwd + "@"
    return ""

def getInitialESNodesString():
    return open("/tmp/es_nodes.txt").readlines()[0].rstrip("\n")

def _getInitialNginxHost():
    return open("/tmp/nginx_host.txt").readlines()[0].rstrip("\n")

def getCurrentESNodesString():
    current_nodes = _getESNodes()
    current_nodes.sort()  
    return "".join(current_nodes)

def testESCluster():
    current_nodes_str = getCurrentESNodesString()
    original_nodes_str = getInitialESNodesString()

    if (current_nodes_str != original_nodes_str):
        raise ValueError("current and original ES node lists don't match, cluster has changed, will redeploy nginx when max failures threshold is reached")

def testNginxInstance():
   current_host = getNginxHost()
   original_host = getInitialNginxHost()
    
   if (current_host != original_host):
        raise ValueError("current and original nginx hosts don't match, nginx has been redeployed")
