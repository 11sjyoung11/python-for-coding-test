import sys
import heapq

def main():
    input = sys.stdin.readline

    N = int(input().strip())  # 카드 묶음 개수 (1 ≤ N ≤ 100,000)

    # 최소 힙(min-heap)에 모든 묶음 크기를 넣는다.
    # heapq는 기본이 최소 힙이므로 가장 작은 두 묶음을 O(log N)으로 꺼낼 수 있다.
    heap = []
    for _ in range(N):
        heapq.heappush(heap, int(input().strip()))  # 묶음 크기: 양의 정수(≤ 1000)

    # 결과(총 비교 횟수). 파이썬 int는 임의 정밀도라 오버플로우 위험 없음.
    total_cost = 0

    # 힙에 원소가 1개면 이미 하나의 묶음이므로 추가 비교(합치기)가 필요 없다 → 비용 0
    # 2개 이상이면, 가장 작은 두 묶음을 뽑아 합치고(비용 추가) 다시 힙에 넣는 과정을 반복
    while len(heap) > 1:
        a = heapq.heappop(heap)   # 가장 작은 묶음
        b = heapq.heappop(heap)   # 두 번째로 작은 묶음
        cost = a + b              # 두 묶음을 합치는 데 드는 비교 횟수(=비용)
        total_cost += cost        # 누적 비용에 더한다

        heapq.heappush(heap, cost)  # 합쳐진 새 묶음을 다시 힙에 넣어 이후 합치기에 참여

    print(total_cost)

if __name__ == "__main__":
    main()

# 시간 복잡도: O(N log N)
#  - 모든 원소 힙 삽입: O(N) ~ O(N log N)
#  - 합치기 반복: (N-1)번 pop/pop/push → 각 단계 O(log N) → 전체 O(N log N)
# 공간 복잡도: O(N) (힙 저장용)