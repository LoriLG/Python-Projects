from tkinter import *
import tkinter as tk

import dbFileTransfer_gui
import dbFileTransfer_func

class ParentWindow(Frame):
     def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(510,100)
        self.master.maxsize(600,200)


        dbFileTransfer_func.center_window(self,510,100)

        self.master.title("DataBase FileTransfer")

        self.master.configure(bg="#F8F8F8")

        self.master.protocol("WM_DELETE_WINDOW", lambda: dbFileTransfer_func.ask_quit(self))
        arg = self.master

        dbFileTransfer_gui.load_gui(self)

if __name__ == "__main__":
            root =tk.Tk()
            App = ParentWindow(root)
            root.mainloop()
            

             



     


        

    
