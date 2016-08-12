import os,json

__all__ = '''
  getMarathonAppJSON
  getMarathonAppPorts
  '''.split()

def getHost(rawHost, port):
    return generateIpAddress(rawHost)

def getHostAndPort(rawHost, port):
    host = generateIpAddress(rawHost)
    host += ":"
    host += str(port)
    return host

def generateIpAddress(host):
    strippedHost = host.strip("ip-")
    return strippedHost.replace("-",".")

def generateIpAddressFromDNS(host):
    return host.split(".")[0].strip("ip-").replace("-",".")

def getMarathonAppJSON(url):
    raw_json = os.popen("curl " + url).read()
    return json.loads(raw_json)

def getMarathonAppHosts(url):
    hosts = ""
    app_json = getMarathonAppJSON(url)
    for app in app_json["app"]["tasks"]:
       hosts += generateIpAddressFromDNS(app["host"])
       hosts += ":"
       hosts += str(app["ports"][1])
       hosts += ","
    
    final_hosts = hosts.strip(",")
    return final_hosts

def getMarathonAppMaster(url):
    master_app = getMarathonAppJSON(url)["app"]["tasks"][0]
    master = master_app["host"]
    master += ":"
    master += str(master_app["ports"][1])
    return master

