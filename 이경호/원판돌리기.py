import sys;sys.stdin=open('원판돌리기.txt')
from pprint import pprint

def _rotate(dq, x, d, k):
    if d:
        dq.rotate(k)
    else:
        dq.rotate(-k)


from collections import deque

N, M, T = map(int, input().split())
rounds = [deque(map(int, input().split())) for _ in range(N)]

pprint(rounds)
# rotate(1) 시계
# rotate(-1) 반시계
