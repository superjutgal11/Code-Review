# 재귀함수를 통한 피보나치 수열 만들기
'''
def func(in_num_local):

    global answer, index

    while (index < in_num_local):
        if index == 0:
            answer.append(0)
        elif index == 1:
            answer.append(1)
        else:
            answer.append(answer[index-2] + answer[index-1])

        index += 1


answer = []  # 값들을 넣을 빈 리스트를 전역변수로 선언
index = 0  # 함수 내에서 값이 들어간 순서를 저장

in_num_wide = int(input("양의 정수를 입력 해 주세요 : "))

while in_num_wide <= 0:
    in_num_wide = int(input("양수를 입력하세요 : "))

func(in_num_wide)
print(answer)
'''


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonacci(n-2)+fibonacci(n-1))


# n = int(input("몇 개의 피보나치수를 원하는가 >> "))
# if n <= 0:
#     n = int(input("양수로 입력 바랍니다 >> "))
# else:
#     print("피보타치 수열 : ", end="")
#     for i in range(n):
#         print(fibonacci(i), end='  ')


# ㅁ = map(int, "10,2", -10.2)
# print(ㅁ)


# def func(n1, n2):
#     return n1+n2


# a = [1, 2, 3, 4, 5]
# b = [10, 15, 16, 17, 19]

# c = map(func, a, b)
# print(list(c))


# def func(a=1, b=1, c=1):
#     return a*b*c


# x = [1, 2, 3, 4, 5, 6, 7, 8]  # 8개 원소
# y = [1, 0, 1, 0, 1, 0, 1]     # 7개 원소
# z = [10, 20, 30, 40, 50]      # 5개 원소

# print(list(map(func, x, y, z)))
