import sys;sys.stdin=open('e-bus.txt')

T = int(input())
for t_case in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    fuel = K
    for i in range(0, len(arr)):
        distance = (arr[i] - arr[i-1]) if i != 0 else arr[i]
        fuel -= distance
        if arr[i] + K >= N and fuel > -1:
            print('#{} {}'.format(t_case, cnt+1))
            break
        elif fuel > 0:
            if fuel - (arr[i+1]-arr[i]) >= 0:continue
            else:
                fuel = K
                cnt += 1
        elif fuel == 0:
            fuel = K
            cnt += 1
        elif fuel < 0:
            print('#{} {}'.format(t_case, 0))
            break

