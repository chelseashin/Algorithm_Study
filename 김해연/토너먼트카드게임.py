def check(x, y):
    if (arr[x] == 1 and arr[y] == 3) or (arr[x] == 1 and arr[y] == 1):
        return x
    elif (arr[x] == 2 and arr[y] == 1) or (arr[x] == 2 and arr[y] == 2):
        return x
    elif (arr[x] == 3 and arr[y] == 2) or (arr[x] == 3 and arr[y] == 3):
        return x
    return y

def match(start, end):
    if start == end:
        return start

    left = match(start, (start+end)//2)
    right = match((start+end)//2+1, end)
    return check(left, right)

TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print("#%d %d" %(tc, match(0, n-1)+1))