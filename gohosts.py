#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
GoHostsLinux   V1.0.0
GHL

GoPlay 工作室
提供hosts文件,android版也由其开发
lerist@163.com

Alonet 工作室
进行GoHostsLinux程序开发
@zsh2401
blog zsh2401.top
e-mail zsh2401@163.com


详情阅读README.MD 或执行程序时传入参数about
READ README.MD TO GET MORE INFO

code = ±500 lines
'''

import platform
'''如果是python2执行本程序,则进行提示并退出'''
python_version = platform.python_version()
if int(python_version[0]) == 2:
    os.system('echo "请使用python3! Please use Python3!"')
    sys.exit()
    

import os
import sys
import time
import urllib.request
import alib
import alib.main_program as mp

'''加载语言文件'''
text = alib.text()

'''检测系统版本'''
if platform.system() != "Linux":
    print(text['please_use_linux'])
    sys.exit()
    
'''检测tkinter状态'''
tk_status = alib.tk_check()
if tk_status == True:
    import tkinter as tk
 
'''检测是否首次运行'''
if alib.f_run():
    with open(sys.path[0] + '/data/install.lock','w') as f_obj:
        f_obj.write(text['del_install_lock'])
    print('create_install_lock')
    alib.radius('?fi=xb')#统计安装人数

'''检测是否有root权限'''
if alib.root_check() == False:
    print(text['need_root'])
    sys.exit()
else:
    print(text['root_ok'])

try:    
    '''根据各种情况创建相应主程序实例'''
    if len(sys.argv) > 1 and sys.argv[1] == '--cmd':#如果参数有--cmd,启动cmd版程序
            gohosts = alib.cmd.CmdProgram()
    elif len(sys.argv) > 1 and sys.argv[1] == '--about':
        print(text['about'])
        sys.exit()
    elif (len(sys.argv) > 1 and sys.argv[1] == '--gui' and tk_status == True) or tk_status == True:#如果传入参数--gui或tk工作正常,则启动gui程序
            window = tk.Tk()
            gohosts = alib.gui.MainGui(window)
    
    else:#否则,运行cmd版程序
        gohosts = alib.cmd.CmdProgram()
        
    '''执行主程序'''
    gohosts.run()

except KeyboardInterrupt:
    print('\n\n' + text['good_bye'] + '\n')
except tk.TclError:
    print(text['no_display'])

    
