import itertools
import requests
import json
from requests.auth import HTTPBasicAuth

def read_files_to_list(files):
    return list(itertools.chain.from_iterable(list(map((lambda file : open(file, "r")\
        .read().splitlines()), files))))

def get_active_usernames(url, proxy):
    basic_auth = HTTPBasicAuth('greg', 'greg')
    headers = {'Accept': 'application/json'}
    proxy_dict = {"html": proxy}
    r = requests.get(url, auth=basic_auth, headers=headers, proxies=proxy_dict)
    print(url)
    result = json.loads(r.content.decode())
    val = []
    for asset in result["Assets"]:
        val.append(asset["Attributes"]["Username"]["value"])
    return val
