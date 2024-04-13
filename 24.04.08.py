# print("값을 입력하세요 : ",end="")

# n = int(input())

# th_li = []
# i = 0

# # while ( (n % 3) < 3 ):
# #     th_li.append(n % 3)
# #     n = n - 3 ** i * th_li[i]
# #     i += 1

# th_li.append(n%3)

# print('입력받은 값의 3진수의 반대형태는 {}입니다.'.format(th_li))

# answer = 0

# for j in th_li:
# 	answer += ( 3 ** j * th_li[j] )

# print('입력받은 값의 10진수는 {}입니다.\n'.format(th_li))


# i = 1
# while True:
#     answer = 1 * i
#     print(answer)
#     if i < 10:
#         break
#     i += 1

my_dict = {
    "name": "jonghwa",
    "age": 22,
    "city": "busan",
    "emial": "jjgjk0408@gmail.com"
}
print(my_dict["name"])plus

my_dict["major"] = "robot controll engineering department"
print(my_dict["major"])
del my_dict["age"]
print(my_dict)

my_dict["univ"] = "gyeongsang N.Univ"
print(my_dict["univ"], my_dict["major"], sep="\n")

f = open("24.04.08.json", 'r')
print(f.read())
