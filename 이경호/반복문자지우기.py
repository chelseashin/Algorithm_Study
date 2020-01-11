import sys;sys.stdin=open('반복문자지우기.txt')
from collections import deque
T = int(input())
def dpop(strs):
    words = deque(strs)
    tmp = deque()
    res = deque()
    for i in range(len(words)-1):
        tmp.append(words.popleft())
        if tmp[-1] == words[0]:
            tmp[-1] = 0
            words[0] = 0
    tmp.append(words.popleft())
    for i in tmp:
        if i != 0:
            res.append(i)
    if res == deque(strs):
        return len(res)
    else:
        return dpop(res)
for t_case in range(T):
    words = input()

    print("#{} {}".format(t_case+1,dpop(words)))
    