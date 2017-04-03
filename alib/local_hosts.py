#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
关于系统中hosts的信息和代码
'''
import sys
import urllib.request
import alib
import os
import shutil
import datetime
import time
import json
class LocalHosts():
    '''本地端hosts'''
    def __init__(self):
        self.text = alib.text()
        self.hosts_lj = '/etc/hosts'#系统hosts路径
        self.update()#更新信息
        
    def update(self):
        '''更新信息'''
        self.ver= self.get_syshosts_ver()#获取系统hosts版本

    def get_syshosts_ver(self):
        '''获取系统Hosts版本信息'''
        print(self.code()[4])
        try:
            if self.code('default')[0].rstrip() == '# Go Hosts' or self.code('default')[0].rstrip()  == '# Go Hosts AD':#如果头为特定字符,则视为是GoHosts的Hosts
                #生成hosts版本
                return (self.code('default')[5][1:].rstrip() + '  ' 
                    + self.text['time'] +':' + self.code('default')[1][1:].rstrip() 
                    + '   \n' + self.text['type'] +': ' 
                    + self.code('default')[4][1:].rstrip())
            else:#否则视为未安装gohosts
                return self.text['unknow_hosts']
        except FileNotFoundError:#报错??权限不足?还是?
            return 'ERROR!!!!!CHECK YOU SYSTEM!!!'

    def code(self,code_type = 'default'):
        '''根据传入参数返回程序系统hosts代码'''
        if code_type == 'default':
            return open(self.hosts_lj).readlines()#将hosts读取为列表并返回
        elif code_type == 'read':
            return open(self.hosts_lj).read()#将hosts读取为一个字符串并返回
