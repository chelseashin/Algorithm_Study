T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    texts = list(input())
    result = []
    for text in texts:
        if(len(result) == 0 or result[-1] != text):
            result.append(text)
        else:
            result.pop()
            
    print("#%d %d" %(tc, len(result)))