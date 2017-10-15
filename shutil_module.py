import shutil
import os
import Tkinter
import ttk
root = Tkinter.Tk()

os.chdir('C:\\')
 

source = r'C:\\Users\\Student\\Desktop\\Folder A'
destination = r'C:\\Users\\Student\\Desktop\\Folder B'


def transferFiles():
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith('.txt'):
                shutil.move(os.path.join(root,file),destination)
                print (file + ' has been transferred from ' + source)
                print ('To ' +str(destination))


ttk.Style().configure("TButton",padding = 8,relief="raised",justify = "CENTER",background="#ccc")
btn = ttk.Button(text = "Transfer Files",command = transferFiles).pack()

root.mainloop()


                                    

  
                           







