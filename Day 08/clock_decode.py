# %%
input=[]
output=[]
with open('input.txt','r') as file:
    for line in file:
        line = line.rstrip()
        split = line.split(' | ',1)
        isplit = split[0].split(' ')
        osplit = split[1].split(' ')
        input.append(isplit)
        output.append(osplit)
for i in range(len(input)):
    for j in range(len(input[0])):
        input[i][j] = frozenset(sorted(input[i][j]))
    for j in range(len(output[0])):
        output[i][j] = frozenset(sorted(output[i][j]))
# %%
#8.1
count = 0
for i in range(len(output)):
    for j in range(len(output[0])):
        if len(output[i][j])==2 or len(output[i][j])==3 or len(output[i][j])==4 or len(output[i][j])==7:
            count+=1
count
# %%
#8.2
ans = 0
for i in range(len(input)):
    d = dict()
    for j in range(len(input[i])):
        if len(input[i][j]) == 2:
            d[input[i][j]] = 1
        if len(input[i][j]) == 3:
            d[input[i][j]] = 7
        if len(input[i][j]) == 4:
            d[input[i][j]] = 4
        if len(input[i][j]) == 7:
            d[input[i][j]] = 8
        if len(input[i][j]) == 6:
            count=0
            for n in range(len(input[0])):
                if input[i][n].issubset(input[i][j]):
                    count+=1
            if count == 3:
                d[input[i][j]] = 0
            if count == 2:
                d[input[i][j]] = 6
            if count == 6:
                d[input[i][j]] = 9
        if len(input[i][j]) == 5:
            subs = 0
            sups = 0
            for n in range(len(input[0])):
                if input[i][n].issubset(input[i][j]):
                    sups+=1
                if input[i][j].issubset(input[i][n]):
                    subs+=1
            if sups == 3:
                d[input[i][j]] = 3
            if subs == 2:
                d[input[i][j]] = 2
            if subs == 4:
                d[input[i][j]] = 5
    num =''
    for j in range(len(output[0])):
        num = num + str(d[output[i][j]])
    ans+=(int(num))
ans
# %%
