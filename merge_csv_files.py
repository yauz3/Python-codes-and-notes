#import os
#import glob
import pandas as pd

def merge_one_after_the_other(csv_file_1,csv_file_2): # alt alta birleştirmek (TR)
    data_1 = pd.read_csv(f"{csv_file_1}", index_col=0)
    data_2 = pd.read_csv(f"{csv_file_2}", index_col=0 )
    result = pd.concat([data_1, data_2])
    result.to_csv("merged_csv_file.csv")

def merge_side_by_side():  # yan yana birleştirmek (TR)
    data_1 = pd.read_csv(f"{csv_file_1}", index_col=0)
    data_2 = pd.read_csv(f"{csv_file_2}", index_col=0)
    result = pd.concat([data_1, data_2], axis=1)
    result.to_csv(f"merge_csv_file.csv")