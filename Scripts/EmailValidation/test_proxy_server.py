import requests
import os

proxy_host = 'global.rotating.proxyrack.net'
proxy_port = 9000
proxy_username = 'ejaz'
proxy_password = 'WR84NKS-BBBY1EG-QXC1CDU-HYYWH3U-ZYPM7ME'


PROXY_RACK_DNS = "global.rotating.proxyrack.net:9000"

urlToGet = "http://api.ipify.org/?format=json"

proxy = {"http":"http://{}:{}@{}".format(proxy_username, proxy_password, PROXY_RACK_DNS)}

r = requests.get(urlToGet , proxies=proxy)

print("Response:\n{}".format(r.text))

#apache library not use
#if not by default then use sockets