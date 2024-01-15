from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
a = list(map(int, input().split()))

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index


#값이 4인 데이터 개수 출력
count = count_by_range(a, x, x)

if count == 0:
    print(-1)
else:
    print(count)