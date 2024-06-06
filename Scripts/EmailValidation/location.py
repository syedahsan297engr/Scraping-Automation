import requests
from requests.auth import HTTPProxyAuth


proxy_host = 'global.rotating.proxyrack.net'
proxy_port = 9000
proxy_username = 'ejaz'
proxy_password = 'WR84NKS-BBBY1EG-QXC1CDU-HYYWH3U-ZYPM7ME'

proxies = {
    'http': 'http://88.198.165.115:48139',
    'https': 'http://88.198.165.115:48139'
}

proxies = {
    'http': f'http://{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_host}:{proxy_port}'
}

auth = HTTPProxyAuth(proxy_username, proxy_password)

# Define headers to mimic a browser request (optional but recommended)

try:
    response = requests.get("https://ipinfo.io/json", proxies=proxies, auth=auth)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
