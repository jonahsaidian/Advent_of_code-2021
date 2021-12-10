#%%
import numpy as np

# %%
with open('input.txt','r') as file:
    fish = np.fromstring(file.readline().rstrip(),dtype=int,sep=',')
# %%
fd =dict()
for i in range(9):
    fd[i] = (fish == i).sum()
# %%
def update(fd):
    fdn =dict()
    for i in range(9):
        fdn[i] = float(fd[((i+1)%9)])
    fdn[6] = fdn[6] + fd[0]
    return fdn
# %%
fd1=fd
for step in range(256):
    fd1 = update(fd1)
np.array(list(fd1.values())).sum()
# %%
