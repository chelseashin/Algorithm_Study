import sys;sys.stdin=open('그래프경로.txt')

def dfs(s):
    visit[s] = 1
    for w in G[s]:
        if not visit[w]:
            dfs(w)

for tc in range(int(input())):
    v, e = map(int, input().split())
    G = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        G[a].append(b)
    s, g = map(int, input().split())
    visit = [0] * (v + 1)
    dfs(s)
    print(f'#{tc+1} {visit[g]}')