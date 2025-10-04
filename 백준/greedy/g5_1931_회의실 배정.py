import sys
input = sys.stdin.readline

N = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 정렬 단계
# 1) 먼저 시작시간(start) 오름차순 정렬을 한다.
#    -> 같은 '끝시간'인 회의들끼리는 이 순서(시작시간 오름차순)가 유지된다.
meetings.sort(key=lambda x: x[0])  # x = (start, end)

# 2) 그 위에 끝시간(end) 오름차순 정렬을 덮어쓴다.
#    -> 전체적으로는 '끝시간'이 먼저 비교되고,
#       '끝시간'이 같은 묶음 내부에서는 1)에서 만들어둔 '시작시간' 오름차순이 유지된다.
#    -> 결과적으로 (end, start) 기준 정렬과 동일한 효과.
meetings.sort(key=lambda x: x[1])  # x = (start, end)

# 선택 단계
# - 가장 일찍 끝나는 회의부터 가능한 한 많이 고른다.
count = 0        # 선택한 회의 개수
end_time = 0     # 마지막으로 선택한 회의의 '끝난 시각'

for start, end in meetings:
    # 현재 회의의 시작이 직전 회의의 끝 이후(같아도 OK)이면 선택
    if start >= end_time:
        count += 1
        end_time = end  # 끝 시각 갱신

print(count)