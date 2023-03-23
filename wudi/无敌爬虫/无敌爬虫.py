# 导入库
import requests
import os
import office
from time import sleep


# 介绍
print('针对某种漏洞制作的程序，请勿用于非法行为。')
# 代码区
# 存储数据的无敌列表
wudi_list = []
# 询问爬几个链接
wudi = input('爬几个链接？')
for x in range(int(wudi)):
    # 询问爬什么链接
    wudi = input('爬什么链接？')
    wudi_list.append(wudi)
# 询问爬几次
wudi = input('爬几次链接？')
wudi_list.append(int(wudi))
# 打印列表
print(wudi_list)
