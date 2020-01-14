import sys;sys.stdin=open('배열최소합.txt')

def solve(d, now):
    global answer
    if now > answer:return
    if d == N:
        answer = min(now, answer)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            solve(d + 1, now + board[d][i])
            visit[i] = 0
    
for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    answer = 0xfffff
    solve(0, 0)
    print(f'#{tc+1} {answer}')