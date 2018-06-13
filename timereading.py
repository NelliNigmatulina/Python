import xlrd, time, datetime
def elbas():

    print("Elbas market")
    FCRN = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
    wb = xlrd.open_workbook(FCRN)
    first_sheet = wb.sheet_by_name('Elspot 2017')

    from datetime import time


    col_time=first_sheet.col_values(colx=0, start_rowx=1, end_rowx=25 )
    x = col_time # a float
    x = int(x * 24 * 3600) # convert to number of seconds
    my_time = time(x//3600, (x%3600)//60, x%60) # hours, minutes, seconds
elbas()
