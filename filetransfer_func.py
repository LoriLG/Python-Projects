import os,shutil,datetime
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from datetime import timedelta
from datetime import datetime
from datetime import date

import filetransfer_main
import filetransfer_gui

os.chdir(r'C:\\')

Now = datetime.now()


def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def browseSource(self):
    source = tk.filedialog.askdirectory()
    self.source.set(source)


def browseDestination(self):
    destination = tk.filedialog.askdirectory()
    self.destination.set(destination)


def copySendFiles(self):
    source = self.source.get()
    destination = self.destination.get()
    
    for root, dirs, files in os.walk(source):
        for file in files:
            modified = os.path.getmtime(source + '\\' + file)
            readDate = datetime.fromtimestamp(modified)
            durationTime = Now - readDate
            
            if file.endswith('.txt'):
                 if durationTime <= timedelta(days = 1):
                    shutil.copy(os.path.join(root,file),destination)
                           
    


if __name__ == "__main__":
    pass
            




        
