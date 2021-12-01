#%%
import numpy as np

#%%
input = np.loadtxt('./input.txt')
# %%
#1.1
count=0
for i in range(len(input)-1):
    if input[i+1]>input[i]:
        count+=1

count
# %%
#1.2
count=0
for i in range(0,len(input)-3):
    if input[i+3]>input[i]:
        count+=1
count
# %%
