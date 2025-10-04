A, B, C, M = map(int, input().split())

fatigue = 0   # 현재 피로도
work = 0      # 처리한 일의 양

for _ in range(24):  # 하루는 24시간
    if fatigue + A <= M:
        # 일을 할 수 있는 경우
        fatigue += A
        work += B
    else:
        # 일을 못하면 쉰다
        fatigue = max(0, fatigue - C)

print(work)