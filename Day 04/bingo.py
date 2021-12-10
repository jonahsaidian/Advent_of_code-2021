#%%
import numpy as np
#%%
a=[]
cards=[]
with open('input.txt','r') as file:
    numstring =file.readline().rstrip()
    rolls = np.fromstring(numstring,dtype=int,sep=',')
    for num,line in enumerate(file):
        a.append([num,line])
        if num % 6 == 0:
            continue
        if num % 6 == 1:
            card = np.fromstring(line.rstrip(),dtype=int,sep=' ')
        else:
            card = np.vstack((card,np.fromstring(line.rstrip(),dtype=int,sep=' ')))
        if num %6 == 5:
            cards.append(card)
        
# %%
def wincheck(card,turn):
    mask = np.isin(card,rolls[:turn])
    for i in range(len(mask)):
        if mask[i,0] and mask[i,1] and mask[i,2] and mask[i,3] and mask[i,4]:
            return True
        elif mask[0,i] and mask[1,i] and mask[2,i] and mask[3,i] and mask[4,i]:
            return True
    return False
# %%
#4.1
winner =[]
for turn in range(len(rolls)):
    for cnum in range(len(cards)):
        if wincheck(cards[cnum],turn):
            winner = [turn,cnum]
            break
    if not winner == []:
        break

winner
# %%
mask = np.isin(cards[winner[1]],rolls[:winner[0]])
nos = cards[winner[1]][~ mask]
nos.sum()*rolls[winner[0]-1]
# %%
#4.2
loser =[]

for turn in range(len(rolls)):
    for cnum in range(len(cards)):
        if wincheck(cards[cnum],turn) and not wincheck(cards[cnum],turn-1):
            loser = [turn,cnum]
            
loser
# %%
mask = np.isin(cards[loser[1]],rolls[:loser[0]])
nos = cards[loser[1]][~ mask]
nos.sum()*rolls[loser[0]-1]
# %%
