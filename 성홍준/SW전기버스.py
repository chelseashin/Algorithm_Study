tt = int(input())
for i in range(tt):
    k, n, m = map(int, input().split())
    charge_loc = list(map(int, input().split()))
    nowLoc = 0
    piv = 0
    result = 0
    flag = True
    while(True):
        nowLoc = nowLoc + k
        #도착시 리턴
        if (nowLoc >= n):
            break
        #충전소 찾기
        if(nowLoc >= charge_loc[piv]):
            while (nowLoc >= charge_loc[piv]):
                piv = piv + 1
                if piv == len(charge_loc):
                    break
        else:
            # 도착실패
            result = 0
            break

        nowLoc = charge_loc[piv-1]
        result+=1


    print(f"#{i+1} {result}")


