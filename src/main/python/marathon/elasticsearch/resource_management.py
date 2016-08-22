import os,json

__all__ = '''
  getMarathonAppJSON
  getMarathonAppPorts
  '''.split()

def getNetworkMode():
    return os.getenv("NETWORK_MODE")

def getTransportBindPort():
    mode = getNetworkMode()
    if mode == "BRIDGE":
        return 9300
    if (mode == "HOST"):
        return int(os.getenv("PORT1"))
    else:
        raise ValueError("The NETWORK_MODE environment variable must equal BRIDGE or HOST")

def getNodeName():
    nodeName = ""
    nodeName += os.getenv("HOST")
    nodeName += ":"
    nodeName += str(os.getenv("PORT0"))
    return nodeName

def getAppNames():
    appNames = os.getenv("APP_NAME")
    if "," in appNames:
        return appNames.split(",")
    return [appNames]

def getAppURL(appName):
    return os.getenv("MARATHON_URL") + "/v2/apps/" + appName

def getHost():
    return os.getenv("HOST")
    
def getMarathonAppJSON(url):
    raw_json = os.popen("curl " + url).read()
    return json.loads(raw_json)

def getMarathonAppHosts():
    appNames = getAppNames()
   
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