#%%
import numpy as np

# %%
with open('input.txt','r') as file:
    a = file.readline().rstrip()
    split = a.split(' -> ',1)
    ri = np.fromstring(split[0],dtype=int,sep=',')
    rf = np.fromstring(split[1],dtype=int,sep=',')
    for i,line in enumerate(file):
        line.rstrip()
        split = line.split(' -> ')
        ri = np.vstack((ri,np.fromstring(split[0],dtype=int,sep=',')))
        rf = np.vstack((rf,np.fromstring(split[1],dtype=int,sep=',')))
# %%
map = dict()
count=0
for i in range(len(ri)):
    if ri[i,0]==rf[i,0]:
        yrange = range(min(ri[i,1],rf[i,1]),max(ri[i,1],rf[i,1])+1)
        x=ri[i,0]
        for y in yrange:
            if (x,y) not in map:
                map[(x,y)] = 0
            map[(x,y)] = map[(x,y)]+1
            if map[(x,y)] ==2:
                count +=1
    if ri[i,1]==rf[i,1]:
        xrange = range(min(ri[i,0],rf[i,0]),max(ri[i,0],rf[i,0])+1)
        y=ri[i,1]
        for x in xrange:
            if (x,y) not in map:
                map[(x,y)] = 0
            map[(x,y)] = map[(x,y)]+1
            if map[(x,y)] ==2:
                count +=1
    #5.2 including diagonals
    if abs((rf-ri)[i,0]) == abs((rf-ri)[i,1]):
        dx = (rf-ri)[i,0]
        dy = (rf-ri)[i,1]
        if dx<0:
            xrange = range(ri[i,0],rf[i,0]-1,-1)
        else:
            xrange = range(ri[i,0],rf[i,0]+1,+1)

        if dy<0:
            yrange = range(ri[i,1],rf[i,1]-1,-1)
        else:
            yrange = range(ri[i,1],rf[i,1]+1,+1)

        for l,y in enumerate(xrange):
            x = xrange[l]
            y = yrange[l]
            if (x,y) not in map:
                map[(x,y)] = 0
            map[(x,y)] = map[(x,y)]+1
            if map[(x,y)] ==2:
                count +=1
count

# %%
