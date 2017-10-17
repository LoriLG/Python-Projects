import os,shutil
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk


import filetransfer_main
import filetransfer_func

def load_gui(self):
    self.lbl_file = tk.Label(self.master,text='Enter the folder name for the files to be checked daily:')
    self.lbl_file.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+E)
    self.lbl_folder = tk.Label(self.master,text='Enter the folder name to receive the copied files:')
    self.lbl_folder.grid(row=3,column=0,padx=(27,0),pady=(10,0),sticky=N+E)
    self.lbl_transfer = tk.Label(self.master,text='Copy the files to the receiving folder:')
    self.lbl_transfer.grid(row=5,column=0,padx=(27,0),pady=(10,0),sticky=N+E)

    self.source = StringVar()
    self.destination = StringVar()

    self.btn_file = tk.Button(self.master,width=16,height=1,text='Browse Source',command=lambda:filetransfer_func.browseSource(self))
    self.btn_file.grid(row=0,column=0,padx=(10,5),pady=(35,10),sticky=E)
    self.btn_folder = tk.Button(self.master,width=16,height=1,text='Browse Destination',command=lambda:filetransfer_func.browseDestination(self))
    self.btn_folder.grid(row=3,column=0,padx=(10,0),pady=(35,10),sticky=E)
    self.btn_transfer = tk.Button(self.master,width=12,height=1,text='Copy Files',command=lambda:filetransfer_func.copySendFiles(self))
    self.btn_transfer.grid(row=5,column=0,padx=(15,0),pady=(35,10),sticky=S+E)

    self.txt_file = tk.Entry(self.master,text='',textvariable = self.source,width=50)
    self.txt_file.grid(row=0,column=1,rowspan=1,columnspan=5,padx=(5,0),pady=(20,0),sticky=W)
    self.txt_folder = tk.Entry(self.master,text='',textvariable = self.destination, width=50)
    self.txt_folder.grid(row=3,column=1,rowspan=1,columnspan=5,padx=(5,0),pady=(20,0),sticky=W)
        



if __name__ == "__main__":
    pass
    
            
