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



DFS와 BFS는 그래프 탐색 알고리즘으로 가장 대표적인 탐색 알고리즘입니다.

그래프란 단순히 노드와 간선을 모아놓은 자료구조로 트리와 비교하자면 다음 표와 같습니다.

![](https://gmlwjd9405.github.io/images/data-structure-graph/graph-vs-tree.png)



## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 1. DFS (깊이 우선 탐색)

* dfs는 스택으로 구현할 수 있습니다.
* 함수의 호출 스택을 사용하여 재귀로 구현한 형태이며, dfs는 사실상 재귀로만 구현하게 됩니다.
* 구현이 간단하고 직관적입니다.
* 조건을 처리할 위치가 명확하므로 백트래킹 문제를 해결할때 상태공간 그래프를 그리고 dfs로 해결하게 됩니다.

```python
def dfs(s):
    visit[s] = 1
    print(s, end=' ')
    for w in G[s]:
        if not visit[w]:
            dfs(w)
```

## 2. BFS (너비 우선 탐색)

* bfs는 큐를 이용한 그래프 탐색 방식으로 그 특성상 여러가지 장점이 생깁니다.
  * 방문 순서가 depth에 정비례하므로, 가중치가 없는 그래프의 최단경로를 구할 수 있습니다.
  * 메모리는 많이 사용하더라도 함수의 호출 오버헤드가 발생하지 않아서 빠릅니다.
  * 같은 이유로 재귀의 depth 제한에서 자유롭습니다.

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

* 방향없은 (양방향) 1차원 그래프를 1차원 리스트로 받는 예시입니다.
* 인접행렬, 딕셔너리 등 다양한 방법으로 받을 수 있습니다.
* Visit 체크는 정점의 수가 많으면 많을 수록 set() 자료구조를 사용하는 편이 효율적입니다. 하지만 visit 배열을 이용한 추가적인 처리가 필요한 경우에는 초기값(보통 False나 0) 으로 초기화된 배열을 사용합시다.

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

