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

def generateIpAddressFromDNS(host):
    return host.split(".")[0].strip("ip-").replace("-",".")

def getHost():
    mode = getNetworkMode()
    if (mode == "BRIDGE"):
        return os.getenv("HOST")
    

def getMarathonAppJSON(url):
    raw_json = os.popen("curl " + url).read()
    return json.loads(raw_json)

def getMarathonAppHosts(url):
    hosts = ""
    app_json = getMarathonAppJSON(url)
    for app in app_json["app"]["tasks"]:
       #hosts += generateIpAddressFromDNS(app["host"])
       hosts += app["host"]
       hosts += ":"
       hosts += str(app["ports"][1])
       hosts += ","
    
    final_hosts = hosts.strip(",")
    return final_hosts