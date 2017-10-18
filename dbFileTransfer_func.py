import os,shutil,datetime,sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from datetime import timedelta,datetime,date


import dbFileTransfer_main
import dbFileTransfer_gui

conn = sqlite3.connect("check_date.db")
c = conn.cursor()

os.chdir(r'C:\\')


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

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS checkFile(datestamp TEXT)")
    

def data_entry():
     c.execute("DELETE FROM checkFile")
     now = datetime.now()
     date = now.strftime("%Y-%m-%d %H:%M:%S")
     c.execute("INSERT INTO checkFile(datestamp) VALUES (?)", (date,))
     conn.commit()
     

def read_from_db(self):
    c.execute("SELECT * FROM checkFile")
    data = c.fetchall()
    self.data.set(data[0][0])
       
    

def browseSource(self):
    source = tk.filedialog.askdirectory()
    self.source.set(source)


def browseDestination(self):
    destination = tk.filedialog.askdirectory()
    self.destination.set(destination)
    


def copySendFiles(self):
    source = self.source.get()
    destination = self.destination.get()
    data = self.data.get()
    now = datetime.now()
    
    for root, dirs, files in os.walk(source):
        for file in files:
            modified = os.path.getmtime(source + '\\' + file)
            readDate = datetime.fromtimestamp(modified)
            durationTime = now - readDate

            
            if file.endswith('.txt'):
                 if durationTime <= timedelta(days = 1):
                    shutil.copy(os.path.join(root,file),destination)
    data_entry()
    read_from_db(self)
    

create_table()

#conn.close()


if __name__ == "__main__":
    pass
            




        
