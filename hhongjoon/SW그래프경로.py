n = int(input())
for _ in range(n):
    V, E = map(int,input().split())
    arr = [[0]*V for i in range(V)]
    for i in range(E): # 간선, 연결관계, Map으로 할지 / 행렬로 할지
        start, end = map(int,input().split())
        arr[start-1][end-1] = 1
    S, G = map(int,input().split())
    #시작
    result = 0
    visited = []
    temp = []
    visited.append(S)
    temp.append(S)
    while(True):
        if len(temp)>0:
            now = temp.pop()-1
            if now+1 == G:
                result = 1
                break
        else:
            break
        for j in range(V):
            if(arr[now][j] == 1 and j+1 not in visited):
                temp.append(j+1)
                visited.append(j+1)
    print(f"#{_+1} {result}")
