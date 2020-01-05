T = int(input())
arr = [0] * T * 2

for i in range(T):
    result = [0] * 10
    m = 0
    num_len = int(input())
    num = list(input())
    num = list(map(int, num))
    for j in range(num_len):
        result[num[j]] += 1
        if result[num[j]] > m:
            m = result[num[j]]
            arr[2*i+1] = m
            arr[2*i] = num[j]
        elif (result[num[j]] == m and num[j] > arr[2*i]):
            arr[2*i] = num[j]
                
for i in range(T):
    print("#%d %d %d" %(i+1, arr[2*i], arr[2*i+1]))