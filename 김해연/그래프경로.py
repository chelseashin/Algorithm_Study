T = int(input())
# �������� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    path = []
    result = 0
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        
    start, end = map(int, input().split())
    path.append(start)
    
    while(len(path) > 0):
        a = path.pop()
        if(end in graph[a]):
            result = 1
            break
        else:
            path += graph[a]
         
    print("#%d %d" %(tc, result))