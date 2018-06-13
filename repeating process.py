import schedule
import time

def job():
        import xlrd
        FCRN = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
        workbook = xlrd.open_workbook(FCRN)
        first_sheet = workbook.sheet_by_name('Elspot 2017')
        data = [[first_sheet.cell_value(r, c) for c in range(first_sheet.ncols)] for r in list(range(1,25))]
        for r in data:
            print(r[1])
job()
