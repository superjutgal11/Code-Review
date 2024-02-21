def 함수_1():
    print("연습중입니다.")

함수_1()



def 함수_2(매개변수1,매개변수2): # 함수 괄호에 넣는 변수
    매개변수1=int(매개변수1)
    매개변수2=int(매개변수2)
    매개변수_합=매개변수1+매개변수2 # 정수형으로 바꿔 값을 더함
    print("두 정수의 합은"+str(매개변수_합)) # str형으로 바꿔서 print

인수1,인수2=input("두 정수를 ,로 구분하여 2개를 입력하세요 : ").split(',')
함수_2(인수1,인수2) # 함수 호출 때 넣는 변수를 인수라 함




def 함수_3(a,b):
    """
a 는 학생의 이름이고, b는 학생의 나이입니다.
    """
    print(a,b)

c="정재형"
d=25
함수_3(c,d)
print(함수_3.__doc__)




def 함수_4():
    return 1 # 값 1을 그냥 반환

def 함수_5():
    return "안녕" # "안녕"을 그냥 반환.

a1=함수_4() # 변수에 넣을 수도 있고
print(a1)
print(함수_5()) # 함수에 직접 넣을수도 있다.

def 함수_6(a,b):
    return a+b

c = 10
d = 20
print(함수_6(c,d)) # 이런 식으로도 가능



# def 함수_8(a,b,c):
#     """a와 b는 연산될 값이고 c는 연산자임."""
#     if c=='+':
#         return "둘의 합은",a+b
#     if c=='-':
#         return "둘의 차는",a-b
#     else:
#         return "연산자는 ","+외 -만 지원함"
    
# z1,z2,z3=input("두 숫자와 연산자(+,-)를 ,로 구분하여 입력 > ").split(",")
# z1=int(z1)
# z2=int(z2)
# x1,x2=함수_8(z1,z2,z3)
# print("{0}{1}".format(x1,x2))




def 함수_9(a):
    if a==1:
        return "리턴값은 1개 입니다"
    elif a==2:
        return "리턴값은","2개 입니다"
    elif a==3:
        return "리턴값은","3개","입니다"
    else:
        return "1~3 까지만 지원합니다."
    
print(함수_9(1))
print(함수_9(2))
print(함수_9(3))


# def fun1(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)

# fun1(10,20,30,40)

# a = [10,20,30,40,50]
# b = 60,70,80,90,100

# print(*a)
# print(*b)



# def fun3(*a):
#     print(a)

# fun3([1,2,3,4,5,6]) # 여기에 *를 안붙이면 튜플형의 리스트가 출력되고


# def fun4(*a):
#     print(a)

# fun4(*[1,2,3,4,5,6]) # 여기에 *를 붙이니 그냥 튜플이 나오네.. 뭐지


# def fun5(args):
#     for arg in args:
#         print(arg)

# a = 10,20,30,40,504
# fun5(a)



# def fun10(*args):
#     for i in args:
#         print(i)

# fun10(10,20,30,40,50)
# a=[1,2,3,4,5]
# fun10(*a)

def score(name,univ,*score):
    print("학생이름:{0},출신대학:{1},".format(name,univ),end="")
    for i in score:
        print(i,end=",")
    print("")

a1,b1,*c1=input("학생 1의 이름,학교,성적을 ,로 구분하여 입력하시오.\n>").split(",")
a2,b2,*c2=input("학생 2의 이름,학교,성적을 ,로 구분하여 입력하시오.\n>").split(",")
score(a1,b1,*c1)
score(a2,b2,*c2)

