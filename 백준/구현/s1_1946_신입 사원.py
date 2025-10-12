import sys
input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 수

for _ in range(T):
    N = int(input().strip())  # 지원자 수
    applicants = []
    for _ in range(N):
        doc, interview = map(int, input().split())
        applicants.append((doc, interview))

    # 1) 서류 기준 오름차순 정렬
    #    같은 서류 순위가 없다고 문제에서 보장(동석차 없음)
    applicants.sort(key=lambda x: x[0])

    # 2) 첫 지원자는 무조건 합격
    #    이유: 서류 1등은 서류에서 누구에게도 지지 않음.
    count = 1
    min_interview = applicants[0][1]  # 지금까지 본 면접 순위의 최솟값(=가장 우수한 면접)

    # 3) 나머지 지원자 순회
    #    현재 면접 순위가 지금까지의 최솟값보다 "작으면" 선발 가능
    #    (작다 = 더 우수. 같을 일은 없음: 동석차 없음)
    for i in range(1, N):
        # 현재 사람의 면접 순위가 기존 최솟값보다 더 좋으면(작으면)
        if applicants[i][1] < min_interview:
            count += 1                # 선발
            min_interview = applicants[i][1]  # 최솟값 갱신

        # 그렇지 않으면(면접이 더 나쁨) 탈락:
        #  - 서류는 이미 뒤(정렬상)라서 불리
        #  - 면접도 기존 최솟값보다 안 좋으니 두 항목 모두 지는 케이스 발생

    # 4) 결과 출력
    print(count)