T = int(input())
# �������� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
for tc in range(1, T + 1):
    texts = list(input())
    result = []
    for text in texts:
        if(len(result) == 0 or result[-1] != text):
            result.append(text)
        else:
            result.pop()
            
    print("#%d %d" %(tc, len(result)))