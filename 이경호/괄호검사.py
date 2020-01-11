import sys;sys.stdin=open('괄호검사.txt')

from collections import deque
for tc in range(int(input())):
    sentence = input()
    q = deque()
    for i in range(len(sentence)):
        if sentence[i] in '(){}':        
            q.append(sentence[i])

    for _ in range(len(q) ** 2):
        if len(q) < 2:break
        if q[0] + q[1] == '()' or q[0] + q[1] == '{}':
            q.popleft()
            q.popleft()
        else:
            q.rotate(-1)
    if q:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 1')