# DFS와 BFS

[TOC]

> 예시 문제
>
> [DFS와 BFS](https://www.acmicpc.net/problem/1260)
>
> ```bash
> $ sample_input
> 4 5 1
> 1 2
> 1 3
> 1 4
> 2 4
> 3 4
> ```
>
> 

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 1. DFS (깊이 우선 탐색)

```python
def dfs(s):
    visit[s] = 1
    print(s, end=' ')
    for w in G[s]:
        if not visit[w]:
            dfs(w)
```

## 2. BFS

```python
def bfs(s):
    q= deque();q.append(s)
    visit[s] = 1
    print(s, end=' ')
    while q:
        here = q.popleft()
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
                print(w, end=' ')
```



## 3. 입력

```python
v, e, s = map(int, input().split())
G = [[] for _ in range(v+1)]
for i in range(e):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in G:
    i.sort()
visit = [0] * (v+1)
dfs(s)
print()
visit = [0] * (v+1)
bfs(s)
```

