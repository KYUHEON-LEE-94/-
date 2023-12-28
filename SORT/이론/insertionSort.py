array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    print("I: ", end='')
    print(i) #첫번째 인덱스부터 시작한다!
    for j in range(i, 0, -1): #인덱스 i부터 1까지(0은 미포함) 1씩 감소하며 반복하는 문법
        print("J: ", end='')
        print(array[j])
        print(array[j - 1])
        if array[j] < array[j - 1]: #자신과 자기 이전의 데이터와 비교한다.
            array[j], array[j - 1] = array[j - 1], array[j] #이전의 데이터가 더 작으면 내가 그 데이터의 왼쪽으로 간다.
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break;

print(array)
