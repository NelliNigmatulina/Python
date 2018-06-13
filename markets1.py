import xlrd, time, datetime, schedule
import  pandas as pd
d = 30
e = 25
f = 75                                  # Battery SOC
SOC = list(range(e, f))                                 # Range for the battery SOC
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

def battery():

    print("Battery SOC = %", d)
    if d < e:                                           # Check SOC  LOOP
        print('Charge the battery')
    elif d > f:
        print('Sell on Elbas')
    else:
        print('Elspot market delivery,'
              'Work with FCR-N')

battery()

def elbas():

    print("Elbas market")
    fcrn = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
    wb = pd.read_excel(fcrn)
    df = pd.read_excel(fcrn,sheet_name='Elspot 2017')

    from datetime import time
    li = []
    col_time = df.col_values(colx=0, start_rowx=1, end_rowx=25)                 # column time
    for cell in col_time:
        data_values = xlrd.xldate_as_tuple(cell, wb.datemode)                           # create a tuple of datetime
        time_value = time(*data_values[3:])                                            # extract from the tuple a data: hours, minutes, seconds
        li.append(time_value)

    col_value = df.col_values(colx=1, start_rowx=1, end_rowx=25)              # better to define it as a list. Remember this link with a data=[]
    for n, cell_value in enumerate(col_value):                                           # this is still not a list of data!
        print(cell_value, li[n])

elbas()
