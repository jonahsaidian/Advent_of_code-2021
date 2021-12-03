#%%
import numpy as np
import pandas as pd

#%%
input = pd.read_csv('./input.txt',header=None,dtype=str)
input=input[0]

# %%
#3.1
count=np.zeros(len(input[0]),dtype=int)
gamma=''
epsilon=''
for i in range(len(input)):
    for j in range(len(count)):
        count[j]+=int(input[i][j])
for i in range(len(count)):
    count[i] = round(count[i]/len(input))
    gamma = gamma +str(count[i])
    epsilon = epsilon + str(int(not count[i]))
gr=0
er=0
for i in range(len(gamma)):
    gr+=2**(i)*int(gamma[-i-1])
    er+=2**(i)*int(epsilon[-i-1])
print(gr*er)
# %%
#3.2
count=np.zeros(len(input[0]),dtype=int)
linput=input.to_list()
for j in range(len(input[0])):
    for i in range(len(linput)):
        count[j]+=int(linput[i][j])
    count[j] = round(count[j]/len(linput)+.1/len(input))
    temp=[]
    for i in range(len(linput)):
        if count[j] == int(linput[i][j]):
            temp.append(linput[i])
    linput = temp
    if len(linput)==1:
        break

count=np.zeros(len(input[0]),dtype=int)
linput2=input.to_list()
for j in range(len(input[0])):
    for i in range(len(linput2)):
        count[j]+=int(linput2[i][j])
    count[j] = round(count[j]/len(linput2)+.1/len(input))
    temp=[]
    for i in range(len(linput2)):
        if int(not count[j]) == int(linput2[i][j]):
            temp.append(linput2[i])
    linput2 = temp
    if len(linput2)==1:
        break
oxr=0
cr=0
for i in range(len(linput[0])):
    oxr+=2**(i)*int(linput[0][-i-1])
    cr+=2**(i)*int(linput2[0][-i-1])
print(oxr*cr)
# %%
