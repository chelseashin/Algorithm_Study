n = int(input())

leftcode = ['{','(']
rightcode = ['}',')']

for _ in range(n):
    stack = []
    result = 0
    isok = True
    line = list(input())
    #print(line)
    for i in range(len(line)):
        if line[i] in leftcode:
            stack.append(line[i])
            continue
        if line[i] in rightcode:
            if len(stack)>0 and stack[-1] in leftcode:
                if leftcode.index(stack[-1]) == rightcode.index(line[i]):
                    stack.pop()
                    continue
            isok = False
            break
    #print(stack)
    if len(stack)>0:
        isok = False
    if(isok):
        result = 1
    print(f"#{_+1} {result}")
