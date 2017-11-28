import os,json

min_num_master_nodes = None
cluster_name = None

__all__ = '''
  getMarathonAppJSON
  getMarathonAppPorts
  '''.split()

def _getEnvVariable(name):
    e_value = os.getenv(name)
    if e_value == None:
        raise ValueError(name + " environment variable must be set")
    return e_value

def _getEnvVariableWithDefault(name,default):
    return os.getenv(name,default)

def getNetworkMode():
    return _getEnvVariableWithDefault("NETWORK_MODE","HOST")

def getTransportBindPort():
    network_mode = getNetworkMode()
    if network_mode == "BRIDGE":
        return 9300
    else:
        return int(_getEnvVariable("PORT1"))

def getHttpPublishPort():
    return int(_getEnvVariable("PORT0"))
      
def getNodeName():
    nodeName = ""
    nodeName += _getEnvVariable("HOST")
    nodeName += ":"
    nodeName += str(_getEnvVariable("PORT0"))
    return nodeName

def _getAppNames():
    appNames = _getEnvVariable("APP_NAME")
    if "," in appNames:
        return appNames.split(",")
    return [appNames]

def getAppURL(appName):
    return _getEnvVariable("MARATHON_URL") + "/v2/apps/" + appName

def getHost():
    return _getEnvVariable("HOST")
    
def getMarathonAppJSON(url):
    raw_json = os.popen("curl " + url).read()
    return json.loads(raw_json)

def getMarathonAppHosts():
    appNames = _getAppNames()
   
    hosts = ""
    for app in appNames:
        url = getAppURL(app)
        app_json = getMarathonAppJSON(url)
        for app in app_json["app"]["tasks"]:
            hosts += app["host"]
            hosts += ":"
            hosts += str(app["ports"][1])
            hosts += ","
    return hosts.strip(",")

def getMarathonESNodes():
    appNames = _getAppNames()
    nodes = list()
    for app in appNames:
        url = getAppURL(app)
        app_json = getMarathonAppJSON(url)
        if app_json == None:
            raise ValueError("The APP_NAME is incorrect, please check and reconfigure")       
        for app in app_json["app"]["tasks"]:
            node = ""
            node += app["host"]
            node += ":"
            node += str(app["ports"][0])
            nodes.append(node)    
    return nodes 

def getMinNumMasterNodes():
    min_num_master_nodes = _getEnvVariableWithDefault("MIN_NUM_MASTER_NODES","1")
    if min_num_master_nodes == None:
        raise ValueError("MIN_NUM_MASTER_NODES environment variable must be set") 
    return min_num_master_nodes

def getDataDirectories():
    return _getEnvVariableWithDefault("DATA_DIRECTORIES","/data")

def getClusterName():
    return _getEnvVariableWithDefault("CLUSTER_NAME","MARATHON-ES-CLUSTER")

def getNodeType():
    node_type = _getEnvVariableWithDefault("ES_NODE_TYPE","DATA_NODE")
    if node_type == "DATA_NODE_ONLY":
        return "-Enode.data=true -Enode.master=false"
    elif node_type == "MASTER_NODE_ONLY":
        return "-Enode.data=false"
    elif node_type == "CLIENT_NODE_ONLY":
        return "-Enode.data=false -Enode.master=false"
    else:
        return "-Enode.data=true"
