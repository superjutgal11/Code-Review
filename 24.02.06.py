# class 이름저장:
#     def __init__(self,이름,나이,성별,학력): # 생성자
#         self.이름 = 이름
#         self.나이 = 나이
#         self.성별 = 성별
#         self.학력 = 학력

# 사원=[]
# 사원[0]=이름저장("김자자",23,"남자","경국대") # 매개변수는 __init__ 에서의 self 매개변수 제외한 수만큼 넣어야만 한다.
# 사원[1]=이름저장("박사사",23,"남자","조대")
# 사원[2]=이름저장("서하하",24,"남자","경국대")
# 사원[3]=이름저장("주승희",21,"여자","서대")
# 사원[4]=이름저장("박진진",25,"남자","하버드대")
# # 사원 1~5 를 이름저장클래스의 객체(=인스턴스)라고 한다.

# for i in 사원:
#     print( "{0}  {1}  {2}  {3}".format(사원[i].이름,사원[i].나이,사원[i].성별,사원[i].학력) )

# class 정보:
#     def __init__(self,이름,나이,국적):
#         self.이름=이름
#         self.나이=나이
#         self.국적=국적

# 학생1=정보("정자자",23,"대한민국")
# 학생2=정보("다나카",25,"일본")
# 학생3=정보("판빙빙",30,"중국")
# 학생4=정보("응우옌",34,"베트남")

# print("{0}의 국적은 {1}이고 {2}살이다.".format(학생1.이름,학생1.국적,학생1.나이))

class 학생_신상정보:
    def __init__(self,이름,주소지,성별):
        self.이름=이름
        self.주소지=주소지
        self.성별=성별

class 학생_학적정보:
    def __init__(self,학력,학교명): # 생성자 포함 모든 클래스 내 메소드에 첫 인자는 self 임 !!!!!!!!
        self.학력=학력
        self.학교명=학교명
    
    def 연구생여부(self,연구생경험):
        self.연구생경험=연구생경험
        print("해당 학생은 {}를 나왔으며 연구실 경험은 {}입니다.".format(self.학교명,self.연구생경험))
    
    def 인턴여부(self,인턴경험):
        self.인턴경험=인턴경험
        print("해당 학생은 {}를 나왔으며 인턴 경험은 {}입니다.".format(self.학교명,self.인턴경험))
        if self.인턴경험 == False: # False는 bool형이기에 ""를 쓰지 않아야 정상적으로 동작하네요잉!!!!
            print("인턴경험이 없는 힉생은 지원받지 않습니다.")
        

# 학생_1=학생_학적정보("고졸","문성고") # 인스턴스 학생_1 만들기
# 학생_1.연구생여부(True)
# 학생_1.연구생여부(False)
# 학생_1.인턴여부(True)
# 학생_1.인턴여부(False)

# 학생_2=학생_학적정보("대졸","경상국립대")
# 학생_2.연구생여부(False)
# 학생_2.인턴여부(False)
'''
해당 학생은 경상국립대를 나왔으며 연구실 경험은 False입니다.
해당 학생은 경상국립대를 나왔으며 인턴 경험은 False입니다.
인턴경험이 없는 힉생은 지원받지 않습니다.
'''

# b = list(range(10))
# b.append(10)
# print(b)
# b.append(11)
# b.append(12)
# print(b)

# class A:
#     def __init__(self):
#         pass

#     def a(self):
#         print("hi")

#     def b(self):
#         self.a()

#     def c(self):
#         a()

# def a():
#     print("hello!!!!")

# 인스턴스=A()
# # 인스턴스.b()
# # 인스턴스.c()
# # a()
    
# print(isinstance(인스턴스,A))

# a = 10
# b = 1
# c = -3
# d = 10.4

# def facto(n):
#     sum=1
#     if isinstance(n,int) == True:
#         if n > -1 :
#             for i in range(1,n-1):
#                 sum*=i
#             print(str(n)+"팩토리얼의 값은"+str(sum))
#         else:
#             print(str(n)+"은 양의 정수 아님")

#     if isinstance(n,int)!=True:
#         print(str(n)+"은 양의 정수가 아님")

# facto(a)
# facto(b)
# facto(c)
# facto(d)

# class 연습:
#     def __init__(self):
#         self.인삿말="안녕하세요"

#     def pr(self):
#         print(self.인삿말)

# pr_cl = 연습()
# pr_cl.pr()

# class Infor:
#     def __init__(self,name,age,univ):
#         self.name = name
#         self.age=age
#         self.univ=univ
    
#     def prin(self):
#         print("{0}은 {1}살이고 {2}학교를 졸업했다.".format(self.name,self.age,self.univ))

# 정재형 = Infor("정재형","25","Gyeongsang N.Univ")
# 정재형.prin()

# print("{0}은 {1}살이고 {2}학교를 졸업했다!!".format(정재형.name,정재형.age,정재형.univ))

# x = [10,20,30]
# print(*x)

# print(*[10,20,30,40])

# def li(a,b,c,d):
#     print(*[a,b,c,d])

# li(10,20,30,40)
# # li(10,20)

# def 가변인수연습(*args):
#     for arg in args:
#         print(arg)

# # 가변인수연습(10,20,30,30,40,40,50)

# class 재형:
#     def __init__(self,*args):
#         for arg in args:
#             print(args[arg])

# 의진 = 재형(*[1,1,0,0,3])

#------------------------ 연습 해 보기 -------------------
'''
클래스에 의해 생성된 인스턴스의 변수를 속성이라 하고 속성은 __init__ 메소드로 초기화를 하여 줌.

class 클래스이름:
    def __init__(self,인자1,인자2 ... )
        self.인자1 = 인자1
        self.인자2 - 인자2
        ...
    
    def 메소드(self)
        코드

클래스에 의해 생성된 함수를 메서드라 하고 메서드는 인스턴스,메서드 로 호출한다,

A = 클래스이름(__init__을 통해 속성을 설정할 매개변수들을 넣기) A라는 이름의 인스턴스 생성
A.메소드 (인스턴스를 통해 해당 인스턴스의 메소드를 호출)

파이썬에서는 자료형도 클래스임.
예를들어 type(int(10)) 은 class(int) 이런식으로 출력됨. int자체가 정수라는 속성을 가진 수들을 표현하는 클래스인 것.
append를 통해 인스턴스에 새로운 값을 맨 끝 인자로 추가할 수 있음.

pass함수는 클래스나 함수에서 쓰이며 내부 구현이 없어도 오류없이 실행되도록 해 주는 코드임.

같은 클래스 내에 메소드가 여럿 있을 때, 안에서 서로 메소드를 실행시키려면 self.메소드 형식을 써야 함. 그냥 메소드만 쓰면 클래스 외부 함수를 찾음.

같은 클래스 내에서 속성 접근 : self.변수이름
클래스 외부에서 인스턴스의 속성에 접근 : 인스턴스.변수이름

isinisance(a,A) 는 a 가 A클래스의 인스턴스인지 확인해 주는 함수임. 결과는 bool 형식으로 출력 됨.

self는 해당 인스턴스 그 자체를 뜻함.
파이썬에서 클래스의 모든 메소드 첫 인자 (__init__포함)는 무조건 self 이다.



'''