# 상하좌우

# number = int(input())
# direction = input().split()

# x,y = 1,1

# for  i in range(0, number):
#     if direction[i] == "L":
#         x -= x
#         if x == 0: x= 1;
#     elif direction[i] == "R":
#         x += x
#         if x == 0: x= 1;
#     elif direction[i] == "U":
#         y -= y
#         if y == 0: y= 1;
#     elif direction[i] == "D":    
#         y += y
#         if y == 0: y= 1;

# print(y,x)

# n = int(input())
# #x가 가로 y를 세로로 놓고푼문제
# x,y = 1,1
# plans = input().split()

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types=['L','R','U','D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             #nx, ny를 내부에서 초기화해서 사용하는것이 파이썬에서는 가능
#             nx = x +dx[i]
#             ny = y+ dy[i]
#     if nx <1 or ny <1 or nx > n or ny > n: #공간의 크기 및 이동의 제약
#         continue
#     x, y = nx, ny
# print(x,y)

# 시각 문제 

# hour = int(input())
# # 파이썬에서 초를 세는방법

# count = 0
# for i in range(hour+1):
#     for j in range(60):
#         for k in range(60):
#             if "3" in str(i) + str(j) + str(k):
#                 count += 1

# print(count)

#나이트 옮기는 경우의 수

# input_data = input()
# row = int(input_data[1])
# #ord는 유니코드 정수값을 return 예) a는 97을 반환
# column = int(ord(input_data[0])) - int(ord('a')) +1

# steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# result = 0

# for step in steps:
#     print(column)
#     next_row = row + step[0]
#     next_column = column + step[1]

#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result +=1

# print(result)
input_data = input()
my_test = list(input_data);
my_test.sort()
total = 0
new = ""
for i in my_test:
    print(ord(i))
    if ord(i) <65:
        total += int(i)
    else: new += str(i)
print(new + str(total))

data = input()
result = []
value = 0

for x  in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

#알파벳을 정렬
result.sort()
#숫자가 하나라도 존재하는 경우 가장뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))
