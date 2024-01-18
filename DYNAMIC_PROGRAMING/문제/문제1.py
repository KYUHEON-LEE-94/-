#나의 답
# n = int(input())
# k = list(map(int, input().split()))
# d = []



# for index in range(n):
#     result = 0
#     for i in range(index, n, 2):
#         result += k[i]
#     d.append(result)

# print(max(d))

#정답
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0] #창고0만 있을때
d[1] = max(array[0], array[1]) #창고1까지 있을때 최적의 수

#창고1까지 최대.. 2까지 최대... 3끼지 최대..를 누적
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d)
print(d[n-1])
