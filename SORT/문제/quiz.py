n, k = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

for _ in range(k):
    array1_min = min(array1)
    array2_max = max(array2)

    if array1_min > array2_max:
        continue
    else: array1[array1.index(array1_min)], array2[array2.index(array2_max)] = array2[array2.index(array2_max)], array1[array1.index(array1_min)]
    print(array1)
    print(array2)

print(f'{sum(array1)}')

# 풀이식
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort() #배열 A는 오름차순 정렬 수행
b.sort() # 배열 B는 내림차순 정렬 수행

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        #두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: break

print(sum(a))
