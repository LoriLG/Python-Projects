from tkinter import *
import tkinter as tk

import dbFileTransfer_main
import dbFileTransfer_func

def load_gui(self):
    self.lbl_file=tk.Label(self.master,text='Source:')
    self.lbl_file.grid(row=0,column=0,sticky=E)
    self.lbl_folder=tk.Label(self.master,text='Destination:')
    self.lbl_folder.grid(row=1,column=0,sticky=E)
    self.lbl_datetime=tk.Label(self.master,text='Last File Check:')
    self.lbl_datetime.grid(row=2,column=0,sticky=E)
    self.lbl_copy=tk.Label(self.master,text='Copy Files:')
    self.lbl_copy.grid(row=5,column=0,sticky=E)

    self.source = StringVar()
    self.destination = StringVar()
    self.data = StringVar()

    self.btn_file=tk.Button(self.master,width=16,height=1,text='Browse Source',command=lambda:dbFileTransfer_func.browseSource(self))
    self.btn_file.grid(row=0,column=16,sticky=S+E)
    self.btn_folder=tk.Button(self.master,width=16,height=1,text='Browse Destination',command=lambda:dbFileTransfer_func.browseDestination(self))
    self.btn_folder.grid(row=1,column=16,sticky=S+E)
    self.btn_copy=tk.Button(self.master,width=6,height=1,text='Copy',command=lambda:dbFileTransfer_func.copySendFiles(self))
    self.btn_copy.grid(row=5,column=1,sticky=W)

    self.txt_file = tk.Entry(self.master,text='',width=50,textvariable = self.source)
    self.txt_file.grid(row=0,column=1,rowspan=1,columnspan=1)
    self.txt_folder = tk.Entry(self.master,text='',width=50,textvariable = self.destination)
    self.txt_folder.grid(row=1,column=1,rowspan=1,columnspan=1)
    self.txt_datetime=tk.Entry(self.master,text='',width=50,textvariable = self.data) 
    self.txt_datetime.grid(row=2,column=1,rowspan=1,columnspan=1)


    dbFileTransfer_func.read_from_db(self)

                



if __name__ == "__main__":
    pass
    
            
