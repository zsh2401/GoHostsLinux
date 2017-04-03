#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
程序运行所需
'''
import os
import sys
import time
import urllib.request
import json
import alib.gui as gui
import alib.cmd as cmd
import alib.install_hosts as install_hosts
import alib.local_hosts as local_hosts
language = 'zh_cn'
api_url = "http://go.alonet.top/api.php"
def text():
    print()
    '''返回一个字典,包含所有文本'''
    with open(sys.path[0] + '/data/'+language+'.json') as f_obj:
        text = json.load(f_obj)
    with open(sys.path[0] + '/README.md','r') as f_obj:
        #~ print(f_obj.readlines())
        text['about'] = f_obj.read()
        text['about_line'] = f_obj.readlines()
    return text

def f_run():
    '''检测是否首次运行'''
    if os.path.exists(sys.path[0] + '/data/install.lock'):
        print('非首次运行')
        return False
    elif os.path.exists(sys.path[0] + '/data/install.lock') == False:
        print("首次运行")
        return True
        
def tk_check():
    '''检测tkinter是否正常工作'''
    try:
        import tkinter as tk
        return True
    except ImportError:
        #~ print('??')
        return False
        
def root_check():
    '''检测是否拥有最高权限'''
    try:#尝试进行一个最高权限的操作
        with open('/gohosts.check','w') as f_obj:
            pass
        os.remove('/gohosts.check')
        return True
    except PermissionError:#如果没有最高权限,则进行提示并退出程序
        return False
        
def radius(r_type):
    '''进行统计
    ?fi=xb
    ?i_type=nr
    ?i_type=na
    '''
    try:
        urllib.request.urlopen(api_url + r_type)
    except:
        print('error')
