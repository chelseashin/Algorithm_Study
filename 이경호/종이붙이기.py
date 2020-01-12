def solve(x):
    if x == N:return 1
    if x > N:return 0
    return solve(x+10) + solve(x+20) * 2

for tc in range(int(input())):
    N = int(input())
    print(f'#{tc+1} {solve(0)}')