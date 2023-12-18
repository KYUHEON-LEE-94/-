# 거스름돈을 주는 방법
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인해야함!
coins = [500, 100, 50, 10]

# 1. coins의 큰 순서대로 계산을 진행한다.
# 2. 동전으로 나눈 몫을 센다.
# 3. 동전으로 나눈 나머지를 그 다음 계산으로 이어간다.

for coin in coins:
    count += n//coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 (예: 1260/500원의 몫)
    n %= coin

print(count)


# 1이 되는 방법
# n, k = map(int, input().split())

# result = 0

# while True:
#     # n이 k로 나눠지는 수가 될떄까지 몇번 빼야하는 가를 계산
#     # 예 n=23, k=3 이라면 target=21, result=2 -- n이 k로 나눠지기 위해서는 2번 빼야함.
#     target = (n//k) * k  # 21  #6
#     result += (n - target)  # 2 #2 + 1
#     n = target

#     # N이 K보다 작을때 반복문 탈출
#     if n < k:
#         break

#     result += 1  # 3 # 4
#     n //= k  # n = 21//6 몫:7 #몫:2
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)

# 3번 문제
# data = input()
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num


# print(result)

# 4번 모함가 길드
# N명의 모함가중 공포도X인 모험가는 X명의 파티를 꾸려야한다.
# 그럴때, N명의 모험가중 몇개의 파티가 꾸려지는가?
howmany = int(input())
afraid = list(map(int, input().split()))
afraid.sort()

result = 0  # 총그룹
count = 0  # 현재 그룹에 포함된 모험가수

for i in afraid:  # 공포도를 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함시킨다.
    if count >= i:  # 현재 그룹에 포함된 모함가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1  # 총 그룹의 수 증가
        count = 0  # 현재 그룹에 포함된 모험가수 초기화

print(result)
