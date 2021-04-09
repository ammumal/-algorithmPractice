#data 입력받기
T = int(input())
d = []
temp = ''
#temp에 문자열 저장해서 list에 저장
for i in range(T):
    r, s = input().split()
    for i in range(len(s)):
        temp += s[i] * int(r)
    d.append(temp)
    temp = ''

#출력
for i in range(len(d)):
    print(d[i])
