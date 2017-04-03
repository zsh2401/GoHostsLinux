#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
cmd版程序和gui版程序都要用的代码
'''
import alib
import os
import sys
import json
import shutil
import time
import urllib.request
import datetime
try:
    import tkinter as tk
except ImportError:
    pass

class MainProgram():
    '''父类,初始化GUI或命令行版程序共用的代码'''
    def __init__(self):
        self.text = alib.text()#初始化文本
        self.api_url = "http://go.alonet.top/api.php"
        self.install_hosts = alib.install_hosts.InstallHosts()#创建webhosts对象
        self.local_hosts = alib.local_hosts.LocalHosts()#创建本地hosts对象
        self.backup_hosts_lj = sys.path[0] + '/data/bak/'#备份路径
        self.hosts_lj = '/etc/hosts'#系统hosts路径
        self.backup = True#是否开启备份
        self.hosts_ver = "请进行选择"
        self.gg = self.install_hosts.info['gg']#公告
        print(self.gg)#显示公告
        
    def update(self):
        '''更新hosts信息'''
        self.local_hosts.update()
        return 0
        
    def get_install_ver(self,hosts_ver = 'nr'):
        '''获取版本信息'''
        return self.install_hosts.info[hosts_ver][0]
        
    def install(self,install_type = "nr"):
        '''传入nr普通安装,传入na安装科学上网+去除广告hosts'''
        try:
            self.code2sys(self.install_hosts.code(install_type))
            return 0
        except:
            return 1

    def code2sys(self,code):
        '''将传入的代码字符串写入系统hosts'''
        self.sys2bak()
        try:
            print(self.text['writing'])
            with open(self.hosts_lj,'w') as hosts_f_obj:#打开系统hosts文件
                hosts_f_obj.write(code)#写入传入的代码
            return 0#返回0,也就是成功
        except ImportError:
            return "w_code2sys_error"#返回失败
            
    def bak2sys(self):
        '''恢复hosts代码为初始代码'''
        if self.backup:
            print(self.text['huifu'])
            if os.path.exists(self.backup_hosts_lj + 'hosts-default'):
                return self.code2sys(open(self.backup_hosts_lj + 'hosts-default','r').read())
            else:
                return self.text['default_hosts_not_found']
            
    def sys2bak(self):
        '''备份当前系统hosts'''
        if self.backup == True:
            print(self.text['backup_hosts'])
            if os.path.exists(self.backup_hosts_lj +'hosts-default') == False:#如果未发现默认hosts备份,则可能是首次使用gohosts,备份
                shutil.copy(self.hosts_lj,self.backup_hosts_lj +'hosts-default')#将默认hosts保存为/etc/hosts.gobackup
                return 0 #返回成功
            else:#如果默认hosts备份存在,说明已经不是第一次使用hosts,无需再备份默认hosts,则备份到程序目录hosts_backup/下
                now_hosts_name = "hosts" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') 
                shutil.copy(self.hosts_lj,self.backup_hosts_lj +str(now_hosts_name))
                return 0#返回成功
        else:
            return "backup_hosts_off"
            
    def install_finish(self,install_type = 'nr',str_type = 'cmd'):
        '''返回安装完成文字'''
        if str_type == 'cmd':
            self.header = self.header_maker()
            alib.radius('?i_type=' + install_type)
            return self.text['finish_msg'] + "\033[1;31mhttps\033[0m://www.google.com"
        else:
            alib.radius('?i_type=' + install_type)
            return self.text['finish_msg_gui']
        
    

if __name__ == "__main__":
    wtf = alib.text['dont42']
    print(wtf)
