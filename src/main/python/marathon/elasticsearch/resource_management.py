import os,json

min_num_master_nodes = None
cluster_name = None
es_java_opts = '-Xms2g -Xmx2g -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+HeapDumpOnOutOfMemoryError -XX:+AlwaysPreTouch -server -Xss1m -Dlog4j.shutdownHookEnabled=false -Dlog4j2.disable.jmx=true'

__all__ = '''
  getMarathonAppJSON
  getMarathonAppPorts
  '''.split()

def _getEnvVariable(name, default=None):
    if default != None:
       return os.getenv(name, default)
    else:
       value = os.getenv(name)
       if value == None:
           raise ValueError(name + " environment variable must be set")
       return value

def getJvmOptions():
    return _getEnvVariable("JVM_OPTIONS",es_java_opts)
    
def getNetworkMode():
    return _getEnvVariable("NETWORK_MODE","HOST")

def getTransportBindPort():
    network_mode = getNetworkMode()
    if network_mode == "BRIDGE":
        return 9300
    else:
        return int(_getEnvVariable("PORT1"))

def getHttpPublishPort():
    return _getEnvVariable("PORT0")
      
def getNodeName():
    nodeName = ""
    nodeName += getHost()
    nodeName += ":"
    nodeName += _getHttpPublishPort()
    return nodeName

def getAppNames():
    appNames = _getEnvVariable("APP_NAME")
    if "," in appNames:
        return appNames.split(",")
    return [appNames]

def getAppURL(appName):
    return _getEnvVariable("MARATHON_URL") + "/v2/apps/" + appName

def getHost():
    return _getEnvVariable("HOST", None)
    
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
    return _getEnvVariable("MIN_NUM_MASTER_NODES","1")
  
def getDataDirectories():
    return _getEnvVariable("DATA_DIRECTORIES","/data")

def getClusterName():
    return _getEnvVariable("CLUSTER_NAME","MARATHON-ES-CLUSTER")

def getNodeType():
    node_type = _getEnvVariable("ES_NODE_TYPE","DATA_NODE")
    if node_type == "DATA_NODE_ONLY":
        return "-Enode.data=true -Enode.master=false"
    elif node_type == "MASTER_NODE_ONLY":
        return "-Enode.data=false"
    elif node_type == "CLIENT_NODE_ONLY":
        return "-Enode.data=false -Enode.master=false"
    else:
        return "-Enode.data=true"
