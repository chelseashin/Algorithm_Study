T = int(input())

for tc in range(1, T + 1):
    arr = list(map(str, input().split()))
    cal = []
    result = 1
    for i in arr:
        if(i.isdigit()):
            cal.append(int(i))
        elif(i == '+' or i == '-' or i == '*' or i == '/'):
            if(len(cal) < 2):
                result = 0
                break
            b = cal.pop()
            a = cal.pop()
            if(i == '+'): cal.append(a+b)
            if(i == '-'): cal.append(a-b)
            if(i == '*'): cal.append(a*b)
            if(i == '/'): cal.append(a/b)
        else:
            if(len(cal) != 1):
                result = 0
    if(result == 0):
        print("#%d error" %tc)
    else:
        print("#%d %d" %(tc, cal[0]))