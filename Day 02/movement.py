#%%
import numpy as np
import pandas as pd

#%%
input = pd.read_csv('./input.txt',header=None)
# %%
#2.1
x=0
y=0
for i in range(len(input)):
    if input.iloc[i][0][0]=='f':
        x+=int(input.iloc[i][0][-1])
    if input.iloc[i][0][0]=='u':
        y+=-int(input.iloc[i][0][-1])
    if input.iloc[i][0][0]=='d':
        y+=int(input.iloc[i][0][-1])

print(x*y)
# %%
#1.2
x=0
y=0
aim=0
for i in range(len(input)):
    if input.iloc[i][0][0]=='f':
        x+=int(input.iloc[i][0][-1])
        y+=aim*int(input.iloc[i][0][-1])
    if input.iloc[i][0][0]=='u':
        #y+=-int(input.iloc[i][0][-1])
        aim+=-int(input.iloc[i][0][-1])
    if input.iloc[i][0][0]=='d':
        #y+=int(input.iloc[i][0][-1])
        aim+=int(input.iloc[i][0][-1])

print(x*y)
# %%
