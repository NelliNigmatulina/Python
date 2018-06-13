def elbas():

    import pandas as pd
    import matplotlib.pyplot as plt

    fcrn = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
    wb = pd.read_excel(fcrn)
    df = pd.read_excel(fcrn,sheet_name='Elspot 2017')



    wb_num = df.set_index('Time/Date')
    wb_num.head()


    idx = wb_num.idxmax()

    p = idx.value_counts()
    p_1= p.sort_values('Time/Date')
    print(p_1)


    p.plot(kind = 'bar')
    plt.show()
elbas()
