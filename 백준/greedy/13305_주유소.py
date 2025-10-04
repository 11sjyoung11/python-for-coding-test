N = int(input()) # 도시 수

roads = list(map(int, input().split()))   # N-1개의 도로 길이
prices = list(map(int, input().split()))  # N개의 주유소 가격

total_cost = 0 # 누적 비용
min_price = prices[0]   # 현재까지 만난 최저 주유가. 시작은 0번 도시의 가격

# i번째 반복은 "도시 i → i+1" 구간을 주행하는 상황.
for i in range(N - 1):  # # 현재 도시의 가격이 더 싸면, 이후 구간부터 이 가격으로 구매하는 것이 최적. 마지막 도시는 주유 불필요
    if prices[i] < min_price:
        min_price = prices[i]
     # 구간 i의 길이만큼 연료를 소비. 해당 연료는 '지금까지의 최저가'로 산다.    
    total_cost += min_price * roads[i]

print(total_cost)


# 시간 복잡도: O(N)