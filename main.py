# -*- coding: UTF-8 -*-
# Author: Andrew Wang
# Date  : 2021-2-28
# Add   : 
#---------------------------import Library--------------------------------------
from tkinter import *
from tkinter import ttk
from dragonmapper import hanzi
#from dragonmapper import transcriptions
import tkinter.font as tkFont
import re
#---------------------------Class of Application--------------------------------
class Application(Frame):
	# this is the class
	def __init__(self,master=None):
		
		super().__init__(master)
		self.master = master
		self.pack()
		# self.createWidget()
		# self.creat_Label()
		self.creat_Tab()
		
	def cut(self,editor, event=None):
		editor.event_generate("<<Cut>>")
	def copy(self,editor, event=None):
	    editor.event_generate("<<Copy>>")
	def paste(self,editor, event=None):
	    editor.event_generate('<<Paste>>')
		
	def createWidget(self):
		self.btn_Quit = Button(self, text='Exit', command=root.destroy)
		self.btn_Quit.pack()
	
	def creat_Label(self):
		# if label01 in i:
		self.label01 = Label(self,text='Bihammer', width=10, height=2, bg="pink",fg='white')
		self.label01.pack(side='left')
		
		#if label02 in j:
		global photo # only global could show the gif
		photo = PhotoImage(file='./mac-details.gif')
		self.label03 = Label(self, image=photo)
		self.label03.pack()
		
		
	def get_pinyin(self,Chinese_text):
		'''
		'''
		Result_pinyin = hanzi.to_pinyin(Chinese_text, delimiter=' ', all_readings=False,accented=True)
		return Result_pinyin

	def get_pinyin_1(self,Chinese_text):
		'''
		'''
		Result_pinyin = hanzi.to_pinyin(Chinese_text, delimiter=' ', all_readings=False,accented=False)
		return Result_pinyin
	def get_ipa(self,Chinese_text):
		'''
		change the Chinest text to IPA
		'''
		Chinese_text_1 =re.sub(r"\d+"," ",self.get_pinyin_1(Chinese_text))
		Result_IPA = hanzi.to_ipa(Chinese_text_1)
		return Result_IPA		
		
	def creat_Tab(self):
		#标签方法
		tab_Control = ttk.Notebook(self)
		tab1 = Frame(tab_Control)
		tab_Control.add(tab1, text='Chinese to IPA')
		
		tab2 = Frame(tab_Control)
		tab_Control.add(tab2, text='Chinese to Pinyin')
		
		tab_Control.grid(ipadx = 8, ipady = 8, padx = 8, pady = 5)
		# tab_Control.pack(expand=1, fill='x')
		
		mk = ttk.LabelFrame(tab1, text='Convert Chinese Hanzi to IPA')
		mk.grid(column=0, row=0, pady=10, sticky='nsew')
		la1 = ttk.Label(mk,text='Pls type the Chinese')
		la1.grid(column=0, row=0, pady=10, sticky='nsew')
		
		# Tab1输入框
		name = StringVar()
		nameEntered = ttk.Entry(mk,width=80, textvariable=name) #绑定输入参数，方便获取到方法
		nameEntered.grid(column=0, row=1, pady=5, sticky='nsew')
		menubar = Menu(mk, tearoff=False)
		nameEntered.bind("<Button-3>", lambda x:rightKey(x, nameEntered))
		
		#增加 右键功能
		def rightKey(event, editor):
		    menubar.delete(0,END)
		    menubar.add_command(label='Cut',command=lambda:self.cut(editor))
		    menubar.add_command(label='Copy',command=lambda:self.copy(editor))
		    menubar.add_command(label='Paste',command=lambda:self.paste(editor))
		    menubar.post(event.x_root,event.y_root)
		
		# Tab1 按钮
		action = ttk.Button(mk, text='Get The Result without tone', width=30, command=lambda:get_Key(name.get()))
		action.grid(column=0, row=2, rowspan=1, ipady=7,pady=5)
		
		# print result of keywords
		result_1 = Text(mk, width=70, height=14)
		result_1.grid(column=0, row=3, pady=5, sticky='nsew')
		result_1.bind("<Button-3>", lambda x:rightKey(x, result_1))
		
		# button event
		def get_Key(url):
			#print result of keywords
			try:
				Kw = self.get_ipa(url)
			except:
				result_1.insert(INSERT, 'Please type the Chinese Word ...\n')
				return
			result1 = 'Pronounciation：'+ Kw + '\n'
			result_1.insert(END, result1)
			result_1.see(END)
		
		# Tab2 下内容
		# 创建Tab2 内容
		mk2 = ttk.LabelFrame(tab2, text='Convert Chinese Hanzi to Pinyin')
		mk2.grid(column=0, row=0, pady=10, sticky='nsew')
		la1 = ttk.Label(mk2,text='Pls type the Chinese')
		la1.grid(column=0, row=0, pady=10, sticky='nsew')
		
		# Tab2输入框
		name_1 = StringVar()
		nameEntered1 = ttk.Entry(mk2,width=80, textvariable=name_1) #绑定输入参数，方便获取到方法
		nameEntered1.grid(column=0, row=1, pady=5, sticky='nsew')
		menubar = Menu(mk2, tearoff=False)
		nameEntered1.bind("<Button-4>", lambda y:rightKey(y, nameEntered1))
		
		# def rightKey(event, editor):
		    # menubar.delete(0,END)
		    # menubar.add_command(label='Cut',command=lambda:self.cut(editor))
		    # menubar.add_command(label='Copy',command=lambda:self.copy(editor))
		    # menubar.add_command(label='Paste',command=lambda:self.paste(editor))
		    # menubar.post(event.x_root,event.y_root)
		
		# Tab2 按钮1
		action = ttk.Button(mk2, text='Get Result with tone', width=25, command=lambda:get_PY(name_1.get()))
		action.grid(column=0, row=2, rowspan=1,padx=2,pady=7,sticky='w')
		
		action_2 = ttk.Button(mk2, text='Get Result without tone', width=25, command=lambda:get_PY_1(name_1.get()))
		action_2.grid(column=0, row=3, rowspan=1, padx=2,pady=9,sticky='w')
		
		# Result
		result_2 = Text(mk2, width=70, height=14)
		result_2.grid(column=0, row=4, pady=5, sticky='nsew')
		result_2.bind("<Button-5>", lambda x:rightKey(x, result_2))
		
				
		# button1 event
		def get_PY(url):
			#print result of keywords
			try:
				Kw1 = self.get_pinyin(url)
			except:
				result_2.insert(INSERT, 'Please type the Chinese Word ...\n')
				return
			result2 = 'Pinyin：'+ Kw1 + '\n'
			# result_2.insert(INSERT, 'The Result is：\n')
			result_2.insert(END, result2)
			result_2.see(END)
			
		# button2 event
		def get_PY_1(url):
			#print result of keywords
			try:
				Kw2 = re.sub(r'\d+',' ',self.get_pinyin_1(url))
				#Kw2 = self.get_pinyin_1(url)
			except:
				result_2.insert(INSERT, 'Please type the Chinese Word ...\n')
				return
			result3 = 'Pinyin：'+ Kw2 + '\n'
			# result_2.insert(INSERT, 'The Result is：\n')
			result_2.insert(END, result3)
			result_2.see(END)
			
if __name__ == '__main__':
	root = Tk()
	root.title('ChineseToPronc')
	root.geometry("600x500+600+300") #bushi *, but x of xyz
	# 缩放
	# root.rowconfigure(1, weight=1)
	# root.columnconfigure(0, weight=1)
	app = Application(master=root)
	# change the default font size
	default_font = tkFont.nametofont("TkDefaultFont")
	default_font.configure(size=12)
	#change logo
	# if ( sys.platform.startswith('win')): 
		# root.iconbitmap('logo-bihammer.ico')
	# else:
	    # logo = PhotoImage(file='logo-bihammer.gif')
	    # root.call('wm', 'iconphoto', root._w, logo)
	# watch the event
	app.mainloop()
	
	
