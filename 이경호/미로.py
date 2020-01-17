import sys;sys.stdin=open('미로.txt')


delta = ((0,1), (1,0), (-1,0), (0,-1))
def dfs(x, y):
    global answer
    visit[x][y] = 1
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:continue
        if board[nx][ny] == 3:
            answer = 1
            return
        if not visit[nx][ny] and board[nx][ny] == 0:
            dfs(nx, ny)

for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                dfs(i, j)
    print(f'#{tc+1} {answer}')
