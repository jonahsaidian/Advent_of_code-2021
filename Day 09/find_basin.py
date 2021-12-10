#%%
import numpy as np
# %%
data =[]
with open('input.txt','r') as file:
    for line in file:
        line = line.rstrip()
        row = []
        for i in range(len(line)):
            row.append(int(line[i]))
        data.append(row)
data = np.array(data)
# %%
data = np.pad(data,pad_width=1, mode='constant', constant_values=10)
#%%
#9.1
risk =0
lps =[]
for i in range(1,data.shape[0]-1):
    for j in range(1,data.shape[1]-1):
        if (
            data[i,j]<data[i-1,j] and
            data[i,j]<data[i+1,j] and
            data[i,j]<data[i,j-1] and
            data[i,j]<data[i,j+1]
        ):
            lps.append([i,j])
            risk+=1+data[i,j]
        
risk
# %%
#9.2
d=dict()
def rec(n,i,j):
    print('checking point {},{}'.format(i,j))
    if data[i,j]==10:
        print('point is on the border')
        return None
    if n not in d:
        print('adding min to dict')
        d[n]=[]
    if '{},{}'.format(i,j) in np.concatenate(list(d.values())):
        print('point already has been added')
        return None
    if data[i,j]!=9:
        print('adding point to dict')
        d[n].append('{},{}'.format(i,j))
        print('continue recursion')
        rec(n,i+1,j)
        rec(n,i-1,j)
        rec(n,i,j-1)
        rec(n,i,j+1)
    return None
        
# %%
d=dict() 
n=0
for i in range(1,data.shape[0]-1):
    for j in range(1,data.shape[1]-1):
        if (
            data[i,j]<data[i-1,j] and
            data[i,j]<data[i+1,j] and
            data[i,j]<data[i,j-1] and
            data[i,j]<data[i,j+1]
        ):
            rec(n,i,j)
            n+=1

#%%
basins = list(d.values())
m1=0
m2=0
m3=0
for i in range(len(basins)):
    l=len(basins[i])
    if l>m1:
        m3=m2
        m2=m1
        m1=l
    elif l>m2 and l<=m1:
        m3=m2
        m2=l
    elif l>m3 and l<=m2:
        m3=l
ans = m1*m2*m3
ans
# %%
