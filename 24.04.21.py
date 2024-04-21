# print("hi" in "hi everyone!!!")

# fruit = ['banana', 'orange', 'apple', 'kiwi']
# print(min(fruit))  # 사전 순서대로 가장 앞
# print(max(fruit))  # 사전 순서대로 가장 뒤
# print(len(fruit))  # 요소의 갯수

# 과일 = ['바나나', '오렌지', '사과', '키위']
# print(min(과일))  # 사전 순서대로 가장 앞
# print(max(과일))  # 사전 순서대로 가장 뒤
# print(len(과일))  # 요소의 갯수

# a = [10, 5, 9, 8.3, 8, 4]
# print(sorted(a))
# print(sorted(a, reverse=True))
# print(sorted(a, reverse=False))

# li = [10, 20, 30, 'a', 'hi', 10]
# print(li.index('a'))
# print(li.index(10))
# if 20 in li:
#     print(li.index(20))

# li = [10, 20, 10, 5, 10, 20, 10]
# print(li.count(10))
# print(li.count(20))

# li_1 = [10, 20, 30]
# li_2 = ['jjh', 'kmh']
# li_1.extend(li_2)  # 원본 데이터의 값을 변환시킴 (반환값 없음)
# print(li_1)
# li_1.extend('5')
# print(li_1)

# li_1 = [1, 1, 1, 1]
# li_1.append([2, 2, 2])
# print(li_1)

# li_1 = [1, 1, 1, 1]
# li_1.extend([2, 2, 2])
# print(li_1)

# li_1 = [1, 1, 1, 1, 1]
# li_1.insert(2, 20)
# print(li_1)
# li_1.insert(2, [3, 3])
# print(li_1)

# li = [10, 10, 20, 30, 10]
# li.remove(10)
# print(li)  # [10, 20, 30, 10] , 앞에서 부터 인자값 1개만 삭제함
# for _ in li:
#     li.remove(10)  # for문으로 모든 인자값 삭제
# print(li)  # [20, 30]

# li = ['jjh', 'gnu', 25, 4]
# li.reverse()
# print(li)  # [4, 25, 'gnu', 'jjh']

# li_1 = [10, 10, 20]
# li_2 = ['jjh', 25, 'gnu']
# li_3 = li_1 + li_2
# print(li_1, li_2, li_3, sep="\n")

'''
[10, 10, 20]
['jjh', 25, 'gnu']
[10, 10, 20, 'jjh', 25, 'gnu']
'''

# li_1 = [10, 10, 10, 20, 20, 20]
# print(li_1 * 3)
# li_2 = li_1 * 2
# print(li_2)

'''
[10, 10, 10, 20, 20, 20, 10, 10, 10, 20, 20, 20, 10, 10, 10, 20, 20, 20]
[10, 10, 10, 20, 20, 20, 10, 10, 10, 20, 20, 20]
'''

# li_1 = [1, 2, 3, 4]
# li_2 = [1, 2, 3, 4]
# li_3 = [4, 3, 2, 1]

# print(li_1 == li_2)
# print(li_1 == li_3)  # 원소는 같더라도 인덱스가 다르면 == 연산자는 false 반환

# '''
# True
# False
# '''

# li_1 = [1, 2, 3, 4, 5, 6]
# li_2 = [1, 2, 3, 5, 5, 6]  # 인덱스 3부터 li_2가 더 큼
# print(li_1 > li_2)  # F
# print(li_1 >= li_2)  # F
# print(li_1 < li_2)  # T
# print(li_1 <= li_2)  # T

# list_a = [1, 2, 3, 4, 5]
# i = 0
# for x in list_a:
#     list_a[i] = x * 10
#     i += 1
# print(list_a)  # [10, 20, 30, 40, 50]

# list_a = [1, 2, 3, 4, 5]
# list_a = [n*10 for n in list_a]
# print(list_a)  # [10, 20, 30, 40, 50]

# list_a = [1, 2, 3, 4, 5]
# list_a = list(map(lambda x: x*10, list_a))  # 람다함수 이용
# print(list_a)  # [10, 20, 30, 40, 50]


# ip = input("'더하기','빼기','곱하기','나누기','제곱' 연산 또는 '종료'를 선택하세요. >>>")
# x = input("첫번째 숫자를 입력하세요>>>")
# y = input("두번째 숫자를 입력하세요>>>")
# if ip==

a = 1
while a != "종료":
    a = input("'더하기','빼기','곱하기','나누기','제곱' 연산 또는 '종료'를 선택하세요. >>> ")
    if a != "종료":
        x = int(input("첫번째 숫자를 입력하세요>>>"))
        y = int(input("두번째 숫자를 입력하세요>>>"))
        if a == "더하기":
            print("더하기 결과 : {}".format(x+y))
        elif a == "빼기":
            print("빼기 결과 : {}".format(x-y))
        elif a == "곱하기":
            print("곱하기 결과 : {}".format(x*y))
        elif a == "나누기":
            print("나누기 결과 : {}".format(x/y))
        elif a == "제곱":
            print("제곱 결과 : {}".format(x**y))
        else:
            pass
