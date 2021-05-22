# 입력 받기
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]
value.reverse()

#동전 개수를 셀 변수 생성
cnt = 0

#동전 개수 세기
for i in value:
    cnt += k//i
    k %= i

#
print(cnt)
