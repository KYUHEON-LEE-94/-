n = int(input())
array= list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열 (LIC)' 문제로 변환
array.reverse()

#DP 테이블 초기화
dp = [1] * n

#현재 i를 기준으로 그 전의 값들과 계~속 비교
for i in range(1, n):
    print(f'==={i}===')
    for j in range(0, i):
        print(f'{array[j] }, {array[i]}')
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

#열외하는 병사의 최소 수를 출력
print(n - max(dp))