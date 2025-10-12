N = int(input())                      # 사진틀 개수
total = int(input())                  # 총 추천 횟수
recs = list(map(int, input().split()))  # 추천받은 학생 번호들

frames = {}  # key: 학생 번호, value: [추천 수, 등록 시점]

for time, student in enumerate(recs):
    # 이미 게시된 학생이면 추천 수만 증가
    if student in frames:
        frames[student][0] += 1
        continue

    # 사진틀이 비어 있으면 새로 추가
    if len(frames) < N:
        frames[student] = [1, time]
        continue

    # 사진틀이 꽉 찼다면 → 삭제 규칙 적용
    # ① 추천 수가 가장 적고 ② 게시된 지 가장 오래된 학생 제거
    remove_target = min(frames.items(), key=lambda x: (x[1][0], x[1][1]))
    del frames[remove_target[0]]

    # 새 학생 추가
    frames[student] = [1, time]

# 남은 학생 번호 오름차순 정렬
result = sorted(frames.keys())

for i in range(len(result)):
    print(result[i], end=' ')