#%%
import numpy as np

# %%
with open('input.txt','r') as file:
    crabs = np.fromstring(file.readline().rstrip(),dtype=int,sep=',')
# %%
#use median for part 1
pos = np.median(crabs)
# %%
abs(crabs - pos).sum()
# %%
#use mean for part 2
p2 = np.floor(np.mean(crabs))

d = abs(crabs-p2)

f = d*(d+1)/2
print(f.sum())
# %%
