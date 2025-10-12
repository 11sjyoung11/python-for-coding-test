n = int(input())  # n 방의 크기
room = [input().strip() for _ in range(n)]  # N줄의 문자열로 방 구조 입력

row_count = 0  # 가로로 누울 수 있는 자리 수
col_count = 0  # 세로로 누울 수 있는 자리 수

# 가로(행 기준) 검사
for i in range(n):
    cnt = 0  # 현재 연속된 '.' 개수
    for j in range(n):
        if room[i][j] == '.':  # 빈칸이면
            cnt += 1
        else:  # 'X'를 만나면 연속이 끊김
            if cnt >= 2:       # 직전까지 연속된 '.'이 2개 이상이면 자리 하나 추가
                row_count += 1
            cnt = 0            # 다시 초기화
    if cnt >= 2:               # 행 끝까지 '.'으로 끝났을 경우 처리
        row_count += 1

# 세로(열 기준) 검사
for j in range(n):
    cnt = 0
    for i in range(n):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                col_count += 1
            cnt = 0
    if cnt >= 2:
        col_count += 1

# 결과 출력
print(row_count, col_count)