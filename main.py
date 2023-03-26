import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
sns.set_theme(style="darkgrid")




disp_df = pd.read_csv("datos/disp_st2ns1.txt.bz2",
    compression="bz2",
    index_col=0)
"""
for field in disp_df:
    
    if field[-3] != "i" and int(field[-3]) != 1:
        disp_df.drop(field, axis=1, inplace=True)

#make a correlation matrix of the dataframe and show it
corr = disp_df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
plt.show()
"""
#explain how to read the matrix
#select the first 10 years of data
train = disp_df.iloc[:10*365]
test = disp_df.iloc[10*365:]
#select the first 15 columns of train 
train_x = train.iloc[:, :15]
print(train_x)
#print the number of elements of train and test
print("train: ", len(train))
print("test: ", len(test))