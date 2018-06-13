def elbas():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt


    fcrn = "C:\\Users\\n6522\\OneDrive - Lappeenrannan Teknillinen Yliopisto\\Master's thesis\\FCRN.xlsx"
    wb = pd.read_excel(fcrn)
    df = pd.read_excel(fcrn,sheet_name='FCR-N_1 2017')

    wb_num = df.set_index('Time/Date')
    wb_num.head()

    p = wb_num.max()
    p1 = p.value_counts()


    p_time = wb_num.idxmax()
    p_time1 = p_time.value_counts()

    print(p_time)
    print(p_time1)

    p_time1.plot(kind = 'bar')
    plt.show()



elbas()
