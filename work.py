import time, schedule
import pandas as pd
d = 65                                 # Battery SOC


localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)


a = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
wb = pd.read_excel(a)
df = pd.read_excel(a,sheet_name='Elspot 2017')

class Scheduler(object):
    def __init__(self, d):
        self.d = d
    def __str__(self):
        return "SOC: " + str(self.d) + "%"
    def battery(self):
        print("Battery SOC = %", d)
        if d < 20:                                           # Check SOC  LOOP
            print('Charge the battery')
        elif d > 80:
            print('Sell')
        else:
            print('Work')
        localtime = time.asctime(time.localtime(time.time()))
        print("Local current time :", localtime)

c = Scheduler(65)
schedule.every(10).seconds.do(Scheduler.battery(self))
print(c)
while True:
    schedule.run_pending()
    time.sleep(5)
