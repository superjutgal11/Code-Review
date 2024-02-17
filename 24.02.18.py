

# 1.시퀀스객체에 들어있는 요소의 순서를 인덱스라 함. 시퀀스 객체에 []를 쓰고 안에 인덱스를 넣어 접근이 가능함
# 2.인덱스는 반드시 0부터 시작함. 문자열의 요소는 문자이기에 인덱스로 접근하면 문자가 나온다. 
# 3.시퀀스 객체에 인덱스 이지정 시 해당 객체의 전체를 뜻하게 된다. 즉 전체를 다 가져올 수 있으며 []도 생략한다.
# 4.[인덱스]는 __getitem__(인덱스)와 같다.

# a = ["char",10,2]
# print(a[0],a[2]) # 1

# b = "안녕하세요! 문자열데이터입니다."
# print(b[0],b[2],b[10]) # 2

# c = [10,-5.4,"dddddd",'23ff']
# print(c) #3

# d = 10,20,"wjdwogud"
# print(d[1],d.__getitem__(1)) #4

'''
슬라이싱

시퀀스객체[시작인덱스:끝인덱스+1] 로 시퀀스 객체 요소를 가져온다.
예를들어 A[3:10] 으로 하면 A의 3번째 요소부터 9번째 요소까지 가져온다.
슬라이스는 음수 인덱스도 가져오며 이때는 끝 인덱스 -1 을 쓴다.

인덱스 증가폭 설정을 원하면 A[시작인덱스:끝인덱스:인덱스증가폭]

'''

# # len 함수를 이용하여 슬라이싱할 수도 있다.
# a = [10,20,30,40,50,60,70,80]
# print(a[0:len(a)]) #len은 1부터 시작하므로 끝에 -1 을 안해도 됨당!!

# 딕셔너리 만들기!!

# a = {'이름':'정재붕','나이':25,'대학':'경상대','취미':'통화하며 걷기','대학':"원광대"}
# print(a)

# 딕셔너리 할당 및 접근하기!!!!ㅎㅎ

# a = {'이름':'정제형','나이':25}
# print(a['이름'])
# print(a['나이'])
# a['학교']="경싱데"
# print(a)

# dic = {"korea":5000,"japan":13000,'china':130000}
# print('japan'in dic)
# print('usa'not in dic)
# print(len(dic))

# a = int(input())
# if a == 10:
#     print("dd")

# if문은 너무 쉬워서 패스하고

# a = 10
# b = 20
# if a >= 10 and b <= 20:
#     print("yes")
# # 더 축약하여
# if a<15<b:
#     print("YYEESS")

# 리스트 = [10,20,30,'안녕']
# 튜플 = 10,20,30,40,50,'한국'
# 문자형 = "대한민국은 아시아에 있다"

# for i in 리스트:
#     print(i,end=" ")
# print()
# for i in 튜플:
#     print(i,end=" ")
# print()
# for i in 문자형:
#     print(i,end=" ")
# print()

# i = 0

# while i<10:
#     print(i)
# #     i+=1

# a = int(input("반복할 횟수 : "))
# i = 0

# while i<a :
#     print(i)
#     i+=1

# import random


# import random

# a = [10,20,0,100]
# b = 5,4,7
# c = "경상대학교"

# print(random.choice(a))
# print(random.choice(b))
# print(random.choice(c))


# a = random.randint(1,6)
# b = random.randint(1,6)
# c = random.randint(1,6)
# print(a,b,c,sep="     ")

# i = 0 
# while i<10:
#     i+=1
#     if i==8:
#         break
#     print(i,end='  ')