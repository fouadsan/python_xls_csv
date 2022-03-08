import pandas as pd
import numpy as np
import csv

try:

    df = pd.read_excel('list_client_yahyaoui.xlsx', 'Sheet1')
    df1 = df.replace(np.nan, '', regex=True)

    data = []

    for index, row in df1.iterrows():
        
        if not str(row[3]).startswith('0'):
            row[3] = f"0{row[3]}"

        row_list = list((row.values[0:-1]))

        row_list.insert(5, "")
        row_list.insert(6, "1")

        for i in range(7, 20):
            row_list.insert(i, "")


        data.append(row_list)
        

    with open('yahyaoui_clients.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    f.close()

except Exception:
    print("somthing went wrong!")