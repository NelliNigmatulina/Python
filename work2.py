import time, schedule
import pandas as pd

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

a = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
wb = pd.read_excel(a)
df = pd.read_excel(a, sheet_name='Elspot 2017')

class sch(object):
    def __init__(self, d):
        self.d = d
        self.jobs = []
    def __str__(self):
        return "SOC: " + str(self.d) + "%"
    def job(self):
        print("This works!")
        if self.d < 20:  # Check SOC  LOOP
            return ('Charge the battery')
        elif self.d > 80:
            return ('Sell')
        else:
            return ('Work')
    #while True:
    #    schedule.run_all(5)
    #   time.sleep(1)

c = sch(65)  # in brackets it should be battery's SOC

#print(time.asctime(time.localtime(time.time())))
#print(sch.job())
#c.job()
schedule.every(5).seconds.do(c.job)
while True:
    schedule.run_pending()
    time.sleep(1)
    print(time.asctime(time.localtime(time.time())))
