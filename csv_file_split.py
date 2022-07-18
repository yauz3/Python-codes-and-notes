import pandas as pd

# read your csv file
data=pd.read_csv("merged_XGB.csv",index_col=0)

# make list of interested columns
listem=[]
for key, value in data.iterrows():
    listem.append(value["Drugbank_id"])

# delete duplicated values in the list
listem = list(dict.fromkeys(listem))

# split csv file based on your list
for drug_id in listem:
    split_data = data[data["Drugbank_id"] == drug_id]
    split_data.to_csv('%s.csv' % drug_id, header=True)