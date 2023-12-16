# -*- coding : utf-8-*-

import pystray
from PIL import Image
from pystray import MenuItem
from connect import has_internet, get_ipv4, connect
import os
from threading import Thread
from iniparser import parser
import time
import logging
import psutil
import webbrowser


config_file = os.path.join(os.getcwd(), "config.ini")
pid_file = os.path.join(os.getcwd(), "pid.txt")
p = parser(config_file)
configs = p.read_dict('config')

f =  open('pid.txt', 'r+', encoding='utf-8')
pid = f.read()
if len(pid) !=0 and psutil.pid_exists(int(pid)):
    print("程序存在")
    os._exit(0)
f.seek(0)
f.write(str(os.getpid()))
f.close()


def status(icon):
    def th():
        ipv4 = get_ipv4()
        if ipv4 is None:
            icon.notify("", f"请手动配置ip地址")
        else:
            if has_internet():
                icon.notify("已连接到CPU", f"当前ip地址为：{ipv4}")
            else:
                connect(configs['username'], configs['password'])
                icon.notify("正在尝试连接到CPU", f"ip地址为：{ipv4}")
    Thread(target=th, daemon=True).start()


menu = (
    MenuItem('状态', status, default=True),
    MenuItem('打开配置文件', lambda: os.startfile(config_file)),
    MenuItem('打开登录页', lambda: webbrowser.open_new_tab('http://p.cpu.edu.cn')),
    MenuItem('退出', lambda: os._exit(0))
)

image = Image.open("icon.png")
icon = pystray.Icon("连接到CPU", image, "连接到CPU", menu)
Thread(target=icon.run, daemon=True).start()


def main(username, password, timeout) -> None:

    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG,
                        filename='connect.log',
                        filemode='a',
                        encoding='utf-8')

    while True:
        if not has_internet():
            logging.info('正在连接')
            connect(username, password)
        else:
            logging.info('已连接')
        time.sleep(int(timeout))

main(**configs)
