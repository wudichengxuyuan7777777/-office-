import os
import socket
from time import sleep
import random

office = 'MC60H-DWD5-H80U9-6V85M-8280D'
op = input('请输入秘钥')
up = random.randint(1, 10000)
oppuls = [up]
while True:
    if op == office:
        print('正确秘钥')
        break
    else:
        print('错误秘钥')
        break
while True:
    if op == office:
        print('正在检测，你需要等待'+str(oppuls[0])+'秒'+'才能检测完成')
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        sleep(oppuls[0])
        print('你的IP是'+str(ip))
    else:
        break
