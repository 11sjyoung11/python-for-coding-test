n = int(input())

total = n # 처음 입력 정수를 초기값으로 설정
count = 0 # Cycle을 count 할 변수
while True:
    a = total // 10 # n의 첫번째 수
    b = total % 10  # n의 두번째 수
    sum_value = a + b # 각 자릿수를 더한 값
    
    # b를 10의 자릿수, sum_value를 1의 자릿수로 만든값으로 갱신
    total = (b * 10) + (sum_value % 10) 
    count += 1 # 1 Cycle 종료되었으므로 cycle값 count
    if total == n: # 처음 입력한 정수와 값이 같으면 반복문 종료
        break

print(count)

# 문자열 풀이하다가 시간초과됨 간단하게 수학 구현으로 풀자