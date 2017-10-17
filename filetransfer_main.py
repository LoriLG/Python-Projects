import os,shutil,datetime
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk


import filetransfer_gui
import filetransfer_func

class ParentWindow(Frame):
     def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(650,350)
        self.master.maxsize(650,350)


        filetransfer_func.center_window(self,500,300)

        self.master.title("FileTransfer")

        self.master.configure(bg="#F8F8F8")

        self.master.protocol("WM_DELETE_WINDOW", lambda: filetransfer_func.ask_quit(self))
        arg = self.master

        filetransfer_gui.load_gui(self)

if __name__ == "__main__":
            root =tk.Tk()
            App = ParentWindow(root)
            root.mainloop()

        

    
