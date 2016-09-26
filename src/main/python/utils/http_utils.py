import urllib2

def getAuthInfo(url, username, password):
    authinfo = urllib2.HTTPPasswordMgrWithDefaultRealm()
    authinfo.add_password(None, url, username, password)
    return authinfo

def getAuthenticatedUrlOpener(url, username, password):
    handler = urllib2.HTTPBasicAuthHandler(getAuthInfo(url,username,password))
    return urllib2.build_opener(handler)

def getAuthenticatedUrlResponse(url, username, password):
    urllib2.install_opener(getAuthenticatedUrlOpener(url,username,password))
    return urllib2.urlopen(url)

def getUrlResponse(url):
    return urllib2.urlopen(url)