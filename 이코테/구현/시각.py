import sys
input=sys.stdin.readline
lst =[3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
cnt=0
n= int(input())
for i in range(n+1): #0~n
    for j in range(60):
        for k in range(60):
            if i in lst or j in lst or k in lst:
                cnt+=1

print(cnt)


# ==== book ====

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)