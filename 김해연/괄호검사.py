T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    texts = list(input())
    arr = []
    for text in texts:
        if(text == '{' or text == '('):
            arr.append(text)
        if(text == '}'):
            if(len(arr) == 0 or arr[-1] != '{'):
                arr.append(text)
                break
            else:
                arr.pop()
        if(text == ')'):
            if(len(arr) == 0 or arr[-1] != '('):
                arr.append(text)
                break
            else:
                arr.pop()      
    print("#%d %d" %(tc, 1 if len(arr) == 0 else 0))