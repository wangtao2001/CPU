# -*- coding : utf-8-*-

import requests
import socket
import subprocess
from typing import Union

def has_internet() -> bool:
    try:
        result = subprocess.run("ping baidu.com -n 1", check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)
    except subprocess.CalledProcessError:
        return False

    return result.returncode == 0


def get_ipv4() -> Union[str, None]:
    addr = socket.getaddrinfo(socket.gethostname(), None)
    for t in addr:
        ip = t[4][0]
        # CPU内网ip地址都是以10.开始，如果配置了其他的内网地址，这一获取方式可能不正确
        if ip.startswith('10.'):
            return ip
    return None


def connect(username, password) -> None:

    url = 'http://192.168.199.21:801/eportal/'

    params = {
        'c': 'Portal',
        'a': 'login',
        'callback': 'dr1003',
        'login_method': '1',
        'user_account': username,
        'user_password': password,
        'wlan_user_ip': get_ipv4(),
        'wlan_user_mac': '',
        'wlan_ac_ip': '',
        'wlan_ac_name': '',
        'jsVersion': '3.3.2',
        'v': '6743'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
        'Host': '192.168.199.21:801',
    }

    requests.get(url, params=params, headers=headers)