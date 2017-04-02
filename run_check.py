#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''此函数开发过程被废弃多次,又重用多次,我很纠结啊!'''
import sys
import time
import os
import alib
def test_root():
    text = alib.text()
    '''检测是否拥有最高权限'''
    try:#尝试进行一个最高权限的操作
        with open('/gohosts.check','w') as f_obj:
            pass
        os.remove('/gohosts.check')
        return True
    except PermissionError:#如果没有最高权限,则进行提示并退出程序
        return False


    

