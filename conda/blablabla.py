import xlrd, time, datetime, schedule
print('It works')
def elbas():
    FCRN = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
    workbook = xlrd.open_workbook(FCRN)
    first_sheet = workbook.sheet_by_name('Elspot 2017')

    col_value=first_sheet.col_values(colx=1, start_rowx=1, end_rowx=25)

    for cell_value in col_value:
        time.sleep(10)
        print(cell_value)
elbas()
