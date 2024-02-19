# 세트 자료형을 배우자

# set_1 = {'정재형','빅분기','N1','ADSP',25}
# print(set_1)

# set_2 = {10,10,100,100,1000}
# print(set_2)

# 가 = {10,20,30}
# 나 = {20,30,40}

# print(가|나,set.union(가,나),sep="   ") # 합집합
# print(가&나,set.intersection(가,나),sep="     ") # 교집합
# print(가-나,set.difference(가,나),sep="     ") # 차집합
# print(가^나,set.symmetric_difference(가,나),sep="     ") # 대칭차집합

# 파일연습 = open('file_1','w')
# 파일연습.write('파일에 문자열쓰기 연습입니다.\n작성일은 24년 2월 19일.')
# 파일연습.close

# 파일연습 = open('file_1','r')
# a = 파일연습.read()
# print(a)
# 파일연습.close()

# file = open('ffff','w')
# a = file.write("안녕하세용 연습중이랍니다")
# file.close() # 여기 괄호 안하면 파일이 만들어지긴 하는디 아래에서 출력이 안된다잉

# file2 = open('ffff','r')
# b = file2.read()
# print(b)
# file2.close()

# with open ("file_practice",'w') as A:
#     A.write("자동 파일 작성 코드 작성 중압나다")

# with open ('file_practice','r') as A:
#     b = A.read()
#     print(b)

'''
import pickle
 
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
 
with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
'''

# import pickle

# 이름 = "정재형"
# 나이 = 23
# 주소 = '경상남도 진주시'
# 점수 = {'제어공학':80,'디지털공학':100,'수학':30}

# with open("file_practie.p",'wb') as 파일객체:
#     pickle.dump(이름,파일객체)
#     pickle.dump(나이,파일객체)
#     pickle.dump(주소,파일객체)
#     pickle.dump(점수,파일객체)

'''
import pickle
 
with open('james.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
# '''
# import pickle

# with open('file_practie.p','rb') as 파일객체:
#     이름 = pickle.load(파일객체)
#     나이 = pickle.load(파일객체)
#     주소 = pickle.load(파일객체)
#     점수 = pickle.load(파일객체)
#     print(이름,나이,주소,점수)

# # 간단히 연습하기
# a = input("파일에 입력할 내용을 작성해 주십시오 > ")
# b = True
# with open('file_pr','w') as A:
#     A.write(a)

#     while(b==True):
#         b = input("파일 작성/열기 기능을 계속하시겠습니까? bool로 입력하시오 > ")

#         if b==False:
#             break

#         c = input("파일 새로 작성 = write1 , 파일 이어서 작성 = write2, 열기 = read 를 입력하시오 > ")

#         if c == 'write1':
#             d = input("새로 작성할 내용을 입력하시오 > ")
#             with open('file_pr','w')as F:
#                 F.write(d)
        
#         elif c == 'write2':
#             d = input("이어서 작성할 내용을 입력하시오 > ")
#             with open('file_pr','a')as F:
#                 F.write(d)

#         elif c == 'read':
#             with open('file_pr','r')as F:
#                 d = F.read()
#                 print(d)

#         else:
#             print("잘못입력하셨습니다.")

# print("프로그램을 종료합니다.")

# 회문판별 프로그램 만들기!!!

# a = input("회문임을 판단할 문자형 값을 입력하시오 > ")
# b = True
# while(b==True):
#     c = len(a) # a 문자값의 길이를 c에 저장함
#     d = 2 # d가 0이나 1이되면 루프종료. 2개씩 줄어들 수 없기 때문임!!!
#     e = 0 # 루프 횟수
#     f = False

#     if a[0]==a[len(a)-1]:
#         e+=1
#         d=c-e*2
#         while(d>2):
#             if a[e]==a[len(c-e)-1]:
#                 e+=1 ; d = c - e * 2
#             elif d==1&0:
#                 f = True
#                 break
#             else:
#                 f = False
#                 break
#     else:
#         f = False

# print("회문 여부는 {}입니다.".format(f))  실 패


# msg = input("희문 검사 문자 입력 : ")
# 여부 = True

# for i in range(len(msg)//2):
#     if msg[i]!= msg[len(msg)-1-i]:
#         여부 = False

# print(여부)



# massage = input("프롬프트 입력 : ")
# x = True

# for i in range(len(massage)//2-1):
#     if massage[i]!=massage[len(massage)-1-i]:
#         x = False
#         break

# print("{0} 메시지의 회문여부는 {1}입니다.".format(massage,x))

'''
N-gram 을 해 보자

내가봤을 때, n의 개수와 출력치의 개수의 관계비교를 해 보면 len(문장)과 n의 관계는

len   n(=2)
5     4       2일 떄 1 차이
6     5

len   n(=3)
5     3       3일 떄 2 차이
6     4

이므로 len-(n-1) 이 출력의 갯수라 생각햇고 실제로 맞았고 갯수가 정해져 있으므로 for문이 좋을것이라 판단함.
'''

# # 재형이 만든 거
# a , b = input("문자열과 n값을 ,로 구분하여 입력하시오 : ").split(',')
# b = int(b)
# c = len(a)-(b-1) # 반복횟수
# i = j = 0 # 루프인덱스 초기화
# d = 0

# for i in range(c): # 끝의 값은 안나오므로 -1을 할 필요가 없다!!!
#     print(a[d:b+d])
#     d+=1


# def fun_1():
#     print("함수 1을 선언")
#     print("함수 사용 연습")

# fun_1()

# def fun_2():
#     pass

# fun_2

# def fun_3(a,b):
#     print(a,b)

# fun_3(3,5)
# fun_3(10,20)

# def fun_4(a):
#     print(a)

# fun_4("안녕하세요")

# def fun_5(a,b):
#     print("{0}의 나이 = {1}".format(a,b))

# c,d=input("이름과 나이를 띄어쓰기로 구분하여 입력 : ").split()
# fun_5(c,int(d))

# def fun_5(a, b):
#     """
#     이 함수는 외부로부터 입력받은 이름과 나이 정보를 가져와 출력해주는 함수입니다.
#     """
#     print("{0}의 나이 = {1}".format(a, b))

# c, d = input("이름과 나이를 띄어쓰기로 구분하여 입력 : ").split()
# fun_5(c,d)
# print(fun_5.__doc__)

# def fun_6(a,b):
#     return(a+b)

# a = fun_6(10,20)
# print(a)

# print(fun_6(10,20))

# def fun_7():
#     return 10

# print(fun_7())

# def fun_8():
#     return "안녕"

# print(fun_8())

# def fun_9(a):
#     if a<=0: # a가 음수일 떄
#         return # 아무일도 일어나지 않고 함수를 빠져나감
#     return print("{0}은 음수가 아니군요!".format(a))

# i=input("정수값을 입력하시오 : ")
# i = int(i)
# fun_9(i)

# 오늘한거 정리를 하자

# 세트형은 파이썬에서 집합과 같다. 원소는 위치가 정해져 있지 않으며, 즉 []로 접근할 수 없다.
# 요소의 중복이 불가능하여 같은 값의 요소를 여러개 넣으면 1개로 간주한다. 
# 합집합,교집합,차집합,대칭차집합의 연산이 가능하다. 연산자는 순서대로 |(=and) &(=or) -(빼기연산) ^(xor:서로 다른 것만 출력)

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a|b,a&b,a-b,a^b,sep='     ')

# 파일 사용
# # 작성 순서 = 파일 열고, 작성하고, 파일닫고
# 파일객체=open('file','w')
# 파일객체.write("안녕하세용\n정재형입니다\n저는 데이터분석을 공부하고 싶습니다.")
# 파일객체.close()

# # 파일 보는 순서 = 파일 열고, 변수설정, 출력, 파일닫고
# 파일객체_2=open('file','r')
# 파일보기=파일객체_2.read()
# print(파일보기)
# 파일객체_2.close()

# 자도으로 파일닫기 = with open('파일이름','파일모드') as 파일객체:
#                 들여쓰기  코드

# with open('file_2','w')as 파일객체:
#     파일객체.write("안녕?? 지금 복습중이야")

# with open('file_2','r')as 파일객체_2:
#     파일보기 = 파일객체_2.read()
#     print(파일보기)

'''
피클링 : 파이썬 객체를 파일에 저장하는 과정
언피클링 : 파일에 저장된 객체를 읽어오는 과정
'''

# import pickle

# 이름='재붕'
# 나이=20
# 학력='대졸'

# with open("file",'wb')as 파일객체:
#     pickle.dump(이름,파일객체)
#     pickle.dump(나이,파일객체)
#     pickle.dump(학력,파일객체)

# with open("file",'rb')as 파일객체_2:
#     이름=pickle.load(파일객체_2)
#     나이=pickle.load(파일객체_2)
#     학력=pickle.load(파일객체_2)
#     print(이름,나이,학력)
    
