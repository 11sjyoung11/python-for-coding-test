def solution(word: str) -> int:
    weights = [781, 156, 31, 6, 1] # 가중치
    idx = {'A':@, 'E':1, 'I':2, 'O':3, 'U':4}| #문자열 인덱스
    ans = 0
    for i, ch in enumerate(word):
        ans += idx[ch] * weights[i]
    return ans + 1 # 자기자신 포함