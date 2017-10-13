import datetime as dt
from datetime import datetime,timedelta

Portland = dt.datetime.now()

def currentTime():
    NewYork = Portland + timedelta(hours=3)
    London = Portland + timedelta(hours=8)

    print 'Portland date and time: ' + str(Portland)
    print 'New York date and time: ' + str(NewYork)
    print 'London date and time: ' + str(London)


def bankStatus():
    time = int(Portland.hour)

    if time <= 18 and time >= 6:
        print 'At present time the Bank in New York is open.'
    else:
        print 'At present time the Bank in New York is closed.'
    if time >= 1 and time <= 13:
        print 'At present time the Bank in London is open.'
    else:
        print 'At present time the Bank in London is closed.'
        
         

 
currentTime()
bankStatus()
