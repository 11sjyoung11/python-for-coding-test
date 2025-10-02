N = int(input())

count = 0

while N > 0:
    # 5로 나누어 떨어지면 5원 동전 최대한 사용
    if N % 5 == 0:
        count += N // 5
        N = 0
    else:
        # 5로 나누어 떨어지지 않으면 2원을 하나 사용하여 남은 금액 줄이기
        N -= 2
        count += 1

# 정확하게 거슬러 줄 수 있는 경우
if N == 0:
    print(count)
# 거슬러 줄 수 없는 경우
else:
    print(-1)