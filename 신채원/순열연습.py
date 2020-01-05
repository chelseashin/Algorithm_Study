# {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)