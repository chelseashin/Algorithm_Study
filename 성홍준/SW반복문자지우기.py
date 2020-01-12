n = int(input())
for _ in range(n):
    line = list(input())
    temp = []
    prev = len(line)
    while(True):
        for i in range(len(line)):
            if len(temp)>0 and temp[-1] == line[i]:
                temp.pop()
                continue
            temp.append(line[i])
        if prev == len(temp):
            break
        prev = len(temp)
        line = temp
        temp = []
    print(f"#{_+1} {prev}")