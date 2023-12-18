def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀함수를 종료합니다.")

recursive_function(1);

#팩토리얼 구현예제
#반복적으로 구현한 n!
def factorial_iteractive(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <=1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적으로 구현:", factorial_iteractive(5))
print("재귀적으로 구현:", factorial_recursive(5))

#최대공약수 계산
def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(192, 162))