#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
GUI程序
'''
import sys
import alib.main_program as mp
try:
    import tkinter as tk
    import tkinter.messagebox as tkm
except:
    pass
class MainGui(mp.MainProgram):
    def __init__(self,master):
        super().__init__()
        self.master = master
        
        master.resizable(False, False)
        #####设置window标题和大小#####
        self.master.title(self.text['title'])
        self.master.geometry('400x470')
        #####设置window标题和大小#####
        
        ###↓一堆字符串↓##########
        #~ self.choice = tk.StringVar()
        self.var = tk.StringVar()#跟踪选项
        self.xuanxiang = ['科学上网','科学上网 + 去广告']#选项
        self.local_hosts_ver = self.local_hosts.ver
        ###↑一堆字符串↑###########
        
        #####↓用一个frame作为纯白色背景↓#####
        self.bg = tk.Frame(self.master,bg= 'white',height =450,width=400)
        self.bg.place(y = 0)
        #####↑用一个frame作为纯白色背景↑#####
        
        ######Logo图片↓######
        self.logo_file = tk.PhotoImage(file = sys.path[0] + '/data/icon.gif')
        self.logo = tk.Label(self.bg,image = self.logo_file,height = 270)
        self.logo.place(y=-40,x=50)
        #####Logo图片↑#####
        
        ####显示内容####
        self.choice_show = tk.Label(self.bg,bg ='white',text = '选择一个选项!!',fg = 'red')
        self.choice_show.place(y=225,x=150)
        
        self.local_hosts_ver_show = tk.Label(self.bg,bg='white',text=self.text['hosts_ver'][2:-3] +'\t'+ self.local_hosts_ver)
        self.local_hosts_ver_show.place(y=280,x=0)
        
        self.gg_show = tk.Label(self.master,bg = 'white',text = self.text["gg"] + self.gg,width = 400)
        self.gg_show.pack(side=tk.BOTTOM)
        
        
        self.web_hosts_ver_show = tk.Label(self.bg,bg='white',text=self.text['web_hosts_ver'] + '\t' + self.get_install_ver())
        self.web_hosts_ver_show.place(y=320,x=0)
        ####内容####
        
        ###主要按钮↓###
        
        
        self.button_install = tk.Button(self.master,text ='一键安装GoHosts!',
            bg = '#1bd1a5',fg = 'white',height = 2,width = 30,command = self.use_install)
        self.button_install.place(y=350,x=90)        
        
        self.button_bak2sys = tk.Button(self.master,text = '恢复默认Hosts!',
            bg ='white',command = self.use_bak2sys)
        self.button_bak2sys.place(y=410,x=90)
        
        self.button_about = tk.Button(self.master,text ='相关信息',bg = 'white',width = 10,command = self.about_messagebox)
        self.button_about.place(y=410,x=230)
        ###主要按钮↑###
        
        ##############↓使用RadioButton作为选项选择的工具↓############
        self.radio_button_0 = tk.Radiobutton(self.master,text = self.xuanxiang[0],
            variable = self.var,
            value = self.xuanxiang[0],
            bg = 'white',
            command = lambda:self.all_update()
            )
        
        self.radio_button_1 = tk.Radiobutton(self.master,text = self.xuanxiang[1],
            variable = self.var,
            value = self.xuanxiang[1],
            bg = 'white',
            command = lambda:self.all_update()
            )
            
        self.radio_button_0.place(y = 250,x = 90)
        self.radio_button_1.place(y =250,x = 180)
        ##############↑使用RadioButton作为选项选择的工具↑############
        
        tkm.showinfo(title=self.text['title'],message=self.install_hosts.info['ggm'])
        
    def all_update(self):
        '''更新信息'''
        self.update()
        self.choice_show.config(text = '您选择了:' + self.var.get() +'Hosts',fg = 'black')
        self.local_hosts_ver_show.config(text=self.text['hosts_ver'][2:-3] +'\t'+ self.local_hosts.ver)
        
    def use_bak2sys(self):
        '''调用恢复的方法'''
        status_code = self.bak2sys()
        if status_code == 0:
            tkm.showinfo(title=self.text['suc'],message=self.text['bak_suc'])
        else:
            tkm.showinfo(title=self.text['failed'],message=self.text['error'] +'\n' +  str(status_code))
        self.all_update()
            
    def use_install(self):
        '''供按钮调用的安装程序'''
        if self.var.get() != "":
            if self.var.get() == '科学上网 + 去广告':
                install_type = 'na'
            elif self.var.get() == '科学上网':
                install_type = 'nr'
            status_code = self.install(install_type)
            print(install_type)
            if status_code == 0:
                tkm.showinfo(title=self.text['title'],message=self.install_finish(install_type,"gui"))
        else:
            tkm.showwarning(title="警告!",message="请选择一个选项!!!")
        self.all_update()
        
    def about_messagebox(self):
        '''用信息框显示相关信息'''
        tkm.showinfo(title = '关于GoHostsLinux!',message = self.text['about'])
    def run(self):
        self.master.mainloop()
    
