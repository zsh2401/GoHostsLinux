#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
命令行程序,用于服务器或tkinter有问题的场景
'''
import alib.main_program as mp
import os
import sys
class CmdProgram(mp.MainProgram):
    '''命令行版程序'''
    def __init__(self):
        super().__init__()
        self.update()
        self.header = self.header_maker()

    def run(self):
        '''运行程序'''
        e_code = 'continue'#用来判断程序完成状态,如果不为continue,则停止循环
        os.system('clear')
        print(self.install_hosts.info['ggm'])
        input(self.text['input_any_key'])
        
        
        while e_code == 'continue':
            os.system('clear')
            choice = input(self.header + self.text['tishi'])#显示选择提示
            if choice == 'msg' or choice == '0':
                '''显示软件信息'''
                os.system('clear')
                print(self.text['about'])
                input(self.text['input_any_key'])
                
            elif choice == '1':
                fuck = '''安装普通版本hosts'''
                print(fuck)
                e_code = self.install('nr')
                if  e_code == 0:
                    self.simple_header()
                    print(self.install_finish())
                else:
                    print(self.text['error']+ e_code)
                    self.bak2sys()

            elif choice == '2':
                fuck = '''安装去附加广告功能版本hosts'''
                print(fuck)
                e_code = self.install('na')
                if  e_code == 0:
                    self.simple_header()
                    print(self.install_finish('na'))
                else:
                    print(self.text['error']+ e_code)
                    self.bak2sys()
                    
            elif choice == '3':
                fuck = '''恢复默认hosts'''
                print(fuck)
                e_code = self.bak2sys()
                if e_code == 0:
                    self.simple_header()
                    print(self.text['huifu_suc'])
                else:
                    print(self.text['error'] + e_code)
            elif choice == '4' or choice == 'exit':
                print(self.text['good_bye'])
                sys.exit()
            else:
                print(self.text['input_error'])
                input(self.text['input_any_key'])
                
    def header_maker(self):
        '''返回一个菜单字符串'''
        return (''+
            self.text['head'] + '\n' + '\033[0m' + 
            '\033[1;34m' + self.text['gg'] + self.install_hosts.info['gg'] + '\033[0m\n' + 
            self.text['-'] + '\n' + '\033[0m' + 
            self.text['hosts_ver'] + self.local_hosts.ver[:2] + '-' + self.local_hosts.ver[8:-10] + self.local_hosts.ver[-10:] + '\n\n' + '\033[0m' + 
            self.text['go_hosts_ver'] + self.install_hosts.info['nr'][0] + '\n' + '\033[0m' + 
            '\033[1;28m' + self.text['cmd_menu'] + '\033[0m'
                )
                
    def simple_header(self):
        '''打印一个简单的显示hosts版本的头文字'''
        os.system('clear')
        self.update()
        print(''+
            self.text['head'] + '\n' +
            self.text['hosts_ver'] + self.local_hosts.ver + '\n'
                )
            
