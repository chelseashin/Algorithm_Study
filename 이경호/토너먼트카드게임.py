import sys;sys.stdin=open('토너먼트카드게임.txt')

def game(a, b): 
    A, B = arr[a-1], arr[b-1]
    vs = {1: 3, 2: 1, 3: 2}    
    if vs[B] == A:return b
    else:return a

def divide(start, end):
    if start == end:return start
    left, right = divide(start, (start + end) //2), divide((start + end) // 2 + 1, end)
    return game(left, right)

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc+1} {divide(1, N)}")

