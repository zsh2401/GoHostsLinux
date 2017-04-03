#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
关于可安装的hosts的信息和代码
'''
import sys
import urllib.request
import alib
import os
import shutil
import datetime
import time
import json
class InstallHosts():
    '''关于可安装的hosts'''
    def __init__(self):
        self.text = alib.text()
        self.api_url = "http://go.alonet.top/api.php"#测试部署到服务器的api
        #~ self.api_url = "http://127.0.0.1/gohostsapi/api.php"#本地测试api
        #~ self.api_url = "sadasdaasdsa"#测试api爆炸情况
        self.local_api_url = 'data/ah/index.json'
        self.info = self.get_api_data()
        self.nr_code = self.get_hosts_code('nr')
        self.na_code = self.get_hosts_code('na')

    def get_api_data(self):
        '''从API获取最新hosts信息'''
        print(self.text['loading_api'])
        try:
            json_data = urllib.request.urlopen(self.api_url).read().decode('utf-8').rstrip()#获取网页数据并解码并去除不必要前后缀
            dict_data = json.loads(json_data)#用json将网页数据转为python字典
            self.status = True#web api状态设置为True
            nr = dict_data['nr']
            na = dict_data['na']
            gg = dict_data['gg']
            return dict_data
        except:#如果出现错误
            self.status = False#web api状态设置为False
            try:
                with open(self.local_api_url,'r') as f_obj:#读取本地hosts文件夹的api
                    return json.loads(f_obj.read().rstrip())#返回json加载的api数据
            except:#出现错误
                print(self.text['error_reinstall'])#打印要求重装的提示
                sys.exit()#退出程序
        else:
            return 'fuck'
            
    def get_hosts_code(self,hosts_type='nr'):
        '''访问传入的url或路径,获取hosts代码'''
        try:#尝试读取web api的数据
            return urllib.request.urlopen(self.info[hosts_type][1]).read().decode('utf-8')#获取网页并获得解码后的代码
        except:#读取失败则
            return open(self.info[hosts_type][1]).read()#读取本地hosts代码
        else:
            return 'get_web_data_error'#发生某个错误,返回错误值

    def code(self,hosts_type = "nr"):
        '''
        根据传入参数返回hosts代码
        normal  返回科学上网hosts代码
        noad    返回科学上网+去广告hosts代码
        '''
        if hosts_type == "na":
            return self.na_code#返回无广告hosts code
        else:
            return self.nr_code#返回普通hosts code
