import os
import socket
from time import sleep
import random
import urllib.request


op = input('请输入秘钥')
up = random.randint(1, 60)
oppuls = [up,'MC60H-DWHD5-H80U9-6V85M-8280D']
while True:
    if op == oppuls[1]:
        print('正确秘钥')
        break
    else:
        print('错误秘钥')
        break
while True:
    if op == oppuls[1]:
        print('正在检测，你需要等待'+str(oppuls[0])+'秒'+'才能检测完成')
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        sleep(oppuls[0])
        print('你的IP是'+str(ip))
        break
    else:
        print('你的IP未正常检查，请关闭代理或重启电脑。')
        break
print('你使用的秘钥是免费秘钥，大部分功能会受到限制，如需付费秘钥请联系作者，一个付费秘钥30/月或99永久')
sleep(60)
