import shutil,os
import datetime
from datetime import timedelta
from datetime import datetime
from datetime import date


os.chdir('C:\\')

source = r'C:\\Users\\Student\\Desktop\\Changed\\'
destination = r'C:\\Users\\Student\\Desktop\\Received'
Now = datetime.now()

def transferFiles():
   
    for root, dirs, files in os.walk(source):
        for file in files:
            modified = os.path.getmtime(source + file)
            readDate = datetime.fromtimestamp(modified)
            durationTime = Now - readDate
            
            if file.endswith('.txt'):
                 if durationTime <= timedelta(days = 1):
                    shutil.copy(os.path.join(root,file),destination)
                     
                  
              
transferFiles()

