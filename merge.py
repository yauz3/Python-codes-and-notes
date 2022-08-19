"""
1) title ları aynı olanlara göre birleştiriyor. bu yüzden merge kullanabilirsin.
2) birden fazla sütun birleştirmek istersen,
#df3=pd.concat([df, df2])
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


#excel_file has PDB ID and Uniprot AC
file="rank.xlsx"
file2="rank_aggregation.xlsx"
df1 = pd.read_excel(file, sheet_name='Sheet1')

#excel_file2
df2= pd.read_excel(file2, sheet_name='rank_aggregation')

print(df1)
print(df2)
df3=pd.merge(df1, df2)
#birden fazla ortak kolon varsa concat kullanman lazım!!!
#df3=pd.concat([df, df2])
print(df3)
df3.to_excel('birleşmiş.xlsx')
