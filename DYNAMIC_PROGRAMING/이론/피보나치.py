#재귀 함수로 해결했을때.
def fibo(x):
    #재귀함수는 언제 멈출지? <- 이게 포인트
    if x == 1 or x == 2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))

#피보나치 수열: DP로 해결
d = [0]*100

#피보나치 함수를 재귀함수로 구현(탑다운 DP [메모나이제이션 기법])
def fiboDP(x):
    print(f'f(${str(x)}) ')
    #종료 조건(1 혹은 2일때 1을 반환)
    if x == 1 or x ==2:
        return 1
    #이미 계산한적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x-2)
    return d[x]

print(fiboDP(99))

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화(바텀 업)
d = [0]*100

# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

#피보나치 함수 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

#