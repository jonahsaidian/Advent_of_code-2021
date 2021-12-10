#%%
input =[]
with open('input.txt','r') as file:
    for line in file:
            input.append(line.rstrip())
#%%
# input = ['[({(<(())[]>[[{[]{<()<>>',
# '[(()[<>])]({[<{<<[]>>(',
# '{([(<{}[<>[]}>{[]{[(<()>',
# '(((({<>}<{<{<>}{[]{[]{}',
# '[[<[([]))<([[{}[[()]]]',
# '[{[{({}]{}}([{[{{{}}([]',
# '{<[[]]>}<{[{[{[]{()[[[]',
# '[<(<(<(<{}))><([]([]()',
# '<{([([[(<>()){}]>(<<{{',
# '<{([{{}}[<[[[<>{}]]]>[]]']
# %%
#10.1
pairs = {'(':')','[':']','{':'}','<':'>'}
errors = []
for i in range(len(input)):
    stack = []
    for j in range(len(input[i])):
        if input[i][j] in ['<','(','[','{']:
            stack.append(input[i][j])
        if input[i][j] in [')','}',']','>']:
            a=stack.pop(-1)
            if pairs[a] == input[i][j]:
                continue
            if a != input[i][j]:
                errors.append(input[i][j])
                break
errors
# %%
pairs = {'(':')','[':']','{':'}','<':'>'}
d = {')':3,']':57,'}':1197,'>':25137}
score = 0
for i in range(len(errors)):
    score +=d[errors[i]]
score
# %%
#10.2
d = {'(':1,'[':2,'{':3,'<':4}
scores = []
for i in range(len(input)):
    score = 0
    stack = []
    for j in range(len(input[i])):
        if input[i][j] in ['<','(','[','{']:
            stack.append(input[i][j])
        if input[i][j] in [')','}',']','>']:
            a=stack.pop(-1)
            if pairs[a] == input[i][j]:
                continue
            if a != input[i][j]:
                break
    if j != len(input[i])-1:
        continue
    if stack:
        for j in range(len(stack)):
            p = stack.pop(-1)
            score = score*5
            score += d[p]
        scores.append(score)

# %%
scores.sort()
i = int( (len(scores)-1)/2   )
mid = scores[i]
mid
# %%
