
# # 정수형 데이터 : 소숫점이 없는 양수와 음수, 그리고 0까지의 모든 값.
# # 실수형 데이터 : 소숫점이 있는 양수와 음수값들.
# print(3,-3,4.1,-9.099,0,3+4/3) # 이런 식으로 한 프린트문에 , 로 구분하여 넣을 수 있음.
# # 출력 : 3 -3 4.1 -9.099 0 4.333333333333333

# # 문자형 데이터는 String 형과 character형이 있는데, 둘 다 "" 또는 '' 로 작성 가능함.
# print("지금 연습중인데요?"*2,'무슨 일이신지'*3)
# # 출력 : 지금 연습중인데요?지금 연습중인데요? 무슨 일이신지무슨 일이신지무슨 일이신지

# # boolean 형은 논리형이라고 알면 된다. True 와 False 의 두 가지 형태로 나뉘어 진다.
# print(2>3) # False
# print(True,False) # 출력 : True False
# print(not(5>3)) # False    낫 연산도 알아 두자구!!

# # 프린트문에서 각각 개체를 구분할 때 , 와 + 가 대표적으로 있는데, 전자는 각각 개체를 띄어쓰기로 구분하고 후자는 띄어쓰기가 없다.
# # 예를들어 문자형으로 출력하는 경우 전자는 출력 대상이 문자열인지 숫자형인지 구분이 없지만 후자는 숫자형인 경우 str()을 넣어 문자형으러 바꿔 출력해야만 한다.
# 이름 = "정재형"
# 나이 = 23
# print(이름,"의 나이는",나이) # 정재형 의 나이는 23
# print(이름+"의 나이는"+str(나이)) # 정재형의 나이는23

'''
개인적으로 산술연산자 중에서 헷갈리는 건 /   //   % 인데 연습 좀 해보자
'''

# print(10/3) #3.3333333333333335
# print(10//3) #3
# print(10%3) #1

# 체인 비교 연산자
# print( a 연산자_1 b 연산자_2 c)
# 에서 a와 b가 연산자_1 로 true 이면서 b 와 c가 연산자_2 로 true 이면 최종적으로 true 를 출력하는 것이다.
# print(1<2<3<4<5>6) # 좌측부터 계속 t 였는데 마지막에 f가 하나 있으므로 바로 false 출력
# == 는 같으면 트루 아니면 폴스
# != 는 다르면 트루 같으면 폴스

# a = 10
# b = 15
# print(str(a)+"와"+str(b)+"는 서로 같음이 "+str(a==b))
# print(a,"와",b,"는 서로 디름이 ",a!=b)

'''
절댓값은 쉽지 abs() 잖어!!
pow함수는 **랑 같다고 보면 됨. 즉 거듭제곱을 도와주는 함수여.
a**b 는 pow(a,b)와 같음.

'''

# # print(4.3**5.3==pow(4.3,5.3)) # true 출력 하하하
# # ㅁ = [13.3,2.7,3.2,4.499999,5.5,6.3,4.5,2.1,4.0,5,10,2.3,3,0.24,-5,2,2]
# # print(max(ㅁ),min(ㅁ))

# print(round(5.4)) # 5    이런식으로 홀수에선 문제 없음
# print(round(5.5)) # 6    이런식으로 홀수에선 문제 없음
# print(round(4.5)) # round to nearest even 라고 하여 파이썬3부터는 짝수.5 에서는 더 짝수에 가깝게 출력되도록 하는 반올림 방식이다 (ㅂㅅ같노)
# print(round(2,5)) # 2    짝수.5 에서는 걍 가까운 짝수가 출력됨 
# print(round(2.50)) # 2    짝수.5 에서는 걍 가까운 짝수가 출력됨 
# print(round(2.6))  # 그래도 2.6 이면 3 출력됨
# # print(round(ㅁ)) # round 함수는 개별적으로 반올림한다, 즉 리스트의 경우에는 for 문으로 하나하나 다 접촉해야 한다.
# # round 에서 반올ㄹㅁ을 하려는 자ㅣ수를 정할 수 있노
# print(round(3.141592,3)) # 세 번째 자리까지 표시. 즉 4번째에서 3번째로 반올림 해 줌.
# print(round(7.141592,-1)) # 10.0
# print(round(72.141592,-2)) # 100.0

# # 내림함수 = floor , 올림함수 = ceil , 제곱근합수 = sqrt() 이노 ㅋㅋ

# ---------ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ--ㅡ-ㅡ-ㅡ-ㅡ-ㅡ-ㅡ--ㅡ-ㅡ-ㅡ-ㅡ- 뿌히히히

''' 이번엔 난수다'''

from random import*
# random() 함수는 기본설정에서 0.0이상 1 미만(즉 1은 생성이 안됨)의 실수형 랜덤값을 만듦     random()
# 여기에 *X 를 하면 0 부터 x 미만의 랜덤 실수값 생성                                  (random()*10)
# 실수 말고 정수값 원하면 int() 붙이면 되것제!?? 0부터 (10-1) 까지임                    (int(random()*10))
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10))

# 이제 여기서 어려움
# a 이상 b 미만의 랜덤 정수형 난수를 출력??
# int(random()*(b-a+1)+a)

# 4 ~ 10범위 출력
# print(int((random()*7)+4))
# print(int((random()*7)+4))
# print(int((random()*7)+4))
# print(int((random()*7)+4))
# print(int((random()*7)+4))

# 50 ~ 70
# print(int((random()*21)+50))
# print(int((random()*21)+50))
# print(int((random()*21)+50))
# print(int((random()*21)+50))
# print(int((random()*21)+50))
# print(int((random()*21)+50))
# print(int((random()*21)+50))

# # 21 ~ 30
# print(int((random()*10)+21))
# print(int((random()*10)+21))
# print(int((random()*10)+21))
# print(int((random()*10)+21))
# print(int((random()*10)+21))
# print(int((random()*10)+21))

# -50 ~ -10 
# print(int((random()*41)-50))
# print(int((random()*41)-50))
# print(int((random()*41)-50))
# print(int((random()*41)-50))
# print(int((random()*41)-50))
# print(int((random()*41)-50))
# print(int((random()*41)-50))

# 근데 위같은 어려운 식 없이도 가능함ㅋㅋㅋ
# randint(a,b) = a 이상 b 이하의 정수 난수 생성. 신기한 것은 b 미만이 아니고 이하임!!!
# print(randint(1,10))
# print(randint(1,10))
# print(randint(1,10))
# print(randint(1,10))
# print(randint(1,10))

# a = '배가 고프다'
# b = "밥은 어딧지"
# print(a+b)
# print(a,b)

# 슬라이싱

# ---------ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

'''
클래스를 알아야 뭘 만들 수 있으므로 클래스 공부를 하겠다!
'''

# 이름_1 = "마린"
# 체력_1 = 10
# 공격력_1 = 5
# print("{0}의 체력은 {1}이고, 공격력은 {2}이다.".format(이름_1,체력_1,공격력_1))

# 이름_2 = "탱크"
# 체력_2 = 150
# 공격력_2 = 35
# print("{0}의 체력은 {1}이고, 공격력은 {2}이다.".format(이름_2,체력_2,공격력_2))

# # 공격 메소드를 만들어 본다
# def 공격명령(이름,방향,공격력):
#     print("{0}유닛이 {1}방향으로 적군을 {2} 공격력으로 공격합니다.".format(이름,방향,공격력))

# 공격명령(이름_1,"서쪽",공격력_1)
# 공격명령(이름_2,"북동쪽",공격력_2)

# 이런식으로 하나하나 만들기엔 만약 유닛이 엄청 많아진다면 힘들어질 것이다. 이래서 클래스를 사용해야 한다고!!

# class 유닛: # 유닛이라는 이름의 클래스를 생성했다.
#     def __init__(self,이름,체력,공격력): # __init__ 은 생성자(초기화 담당 메소드)임.
#         self.이름 = 이름 # 받아 온 인자를 self를 통해 각 인스턴스의 값으로 초기화한다.
#         self.체력 = 체력
#         self.공격력 = 공격력
#         print("{0}의 체력은 {1}이고, 공격력은 {2}이다.".format(self.이름,self.체력,self.공격력))

# 마린_1=유닛("마린",40,5) # 마린_1 이라는 이름의 인스턴스(=오브젝트)
# 마린_2=유닛("마린",40,5) # 마린_2 이라는 이름의 인스턴스(=오브젝트)
# 마린_3=유닛("마린",40,5) # 마린_3 이라는 이름의 인스턴스(=오브젝트)
# 탱크_1=유닛("탱크",150,35) # 탱크_1 이라는 이름의 인스턴스(=오브젝트)
# 탱크_2=유닛("탱크",150,35) # 탱크_2 이라는 이름의 인스턴스(=오브젝트)

# 위처럼 하나의 클래스로 연관이 있는(위의 다섯 객체들은 모두 이름과, 체력과, 공격력이라는 연관성이 있다)변수들을 생성했다.
# 인스턴스란 클래스의 실체화된 대상이다. 즉 인스턴스는 객체(오브젝트)이다.
# self.변수 는 인스턴스 자체의 변수를 뜻한다.


# __init__ 에 대한 설명!!!!!!!!!!!!!!!!!!!!!!
# __init__ 는 컨스트럭터라고 불리는 초기화용 메소드이다. 인스턴스화할 때, 반드시 처음에 호출되는 특이한 함수이며
# 오브젝트 생성(=인스턴스 생성)시 데이터의 초기화를 실시하는 메소드. 반드시 첫 번째 인수로 self로 지정해야만 한다.
# __init__ dml 첫 인자로 self를 지정하지 않으면 이 클래스로 생성된 인스턴스 자체가 할당이 안된다. 반드시 지정해야 함.

# class 유닛: # 유닛이라는 이름의 클래스를 생성했다.
#     def __init__(self,이름,체력,공격력): # __init__ 은 생성자(초기화 담당 메소드)임.
#         self.이름 = 이름 # 받아 온 인자를 self를 통해 각 인스턴스의 값으로 초기화한다.
#         self.체력 = 체력
#         self.공격력 = 공격력
#         print("{0}의 체력은 {1}이고, 공격력은 {2}이다.".format(self.이름,self.체력,self.공격력))

# 레이스=유닛("레이스",80,5) # 레이스라는 인스턴스에 각각 값이 들어가게 된 상태
# print("{0}의 체력은 {1}이고, 공격력은 {2}이다.".format(레이스.이름,레이스.체력,레이스.공격력)) # 레이스에 값이 들어간 상태이므로 불러오기 가능

# '''
# 레이스의 체력은 80이고, 공격력은 5이다.    클래스 내부에서 출력
# 레이스의 체력은 80이고, 공격력은 5이다.    클래스 외부에서 출력
# '''

# 레이스_2=유닛("하이재킹당한 레이스",80,5)
# 레이스_2.클로킹=True # 새로운 멤버 변수(객체 변수, 인스턴스 변수)를 갖다 붙이고 초기화했다
# if 레이스_2.클로킹 == True:
#     print("현재 {0}는 클로킹 상태입니다.".format(레이스_2.이름)) 
# # 레이스_2.name은 클래스에서 만들어진 변수고, 레이스_2.클로킹은 외부에서 만들어진 변수다
# '''
# 하이재킹당한 레이스의 체력은 80이고, 공격력은 5이다.
# 현재 하이재킹당한 레이스는 클로킹 상태입니다.
# '''
# 요약하면 클래스 외부에서 원하는 객체에 대해 추가적인 변수할당이 가능하고, 확장된 변수는 할당된 객체에서만 사용 가능(ㅈㄴ당연한 말임ㅋㅋ)



class 유닛: # 유닛이라는 이름의 클래스를 생성했다.
    def __init__(self,이름,체력,공격력): # __init__ 은 생성자(초기화 담당 메소드)임.
        self.이름 = 이름 # 받아 온 인자를 self를 통해 각 인스턴스의 값으로 초기화한다.
        self.체력 = 체력
        self.공격력 = 공격력
        print("{0}의 체력은 {1}이고, 공격력은 {2}이다.".format(self.이름,self.체력,self.공격력))

# self 는 생성된 해당 객체 그 자체를 의미하며, 클래스 내 모든 메소드 인자로 반드시 들어간다.
class 유닛을공격:
    def __init__(self,이름,체력,공격력):
        self.이름 = 이름 # self가 없는 변수는 해당 객체로부터 받은 인자를 뜻함
        self.체력 = 체력
        self.공격력 = 공격력
    
    def 공격(self,방향): # 공격 메소드에서도 첫 인자가 self 임을 알 수 있다. 
        print("{0}유닛이 {1}방향으로 {2}공격력으로 공격합니다.".format(self.이름,방향,self.공격력))
        # 방향은 직접 인자를 넣을거임. __init__에서 self로 선언이 안 돼 있으니 self. 를 안쓰는 거임
    
    def 공격받음(self,공격력):
        print("{0}이 {1}의 데미지를 받았습니다.".format(self.이름,공격력))
        self.체력 -= 공격력
        if self.체력<=0:
            print("{0}가 살해/파괴 되었습니다.".format(self.이름))
        print("{0}의 현재 체력은{1}입니다.".format(self.이름,self.체력))
        

파이어뱃 = 유닛을공격("파이어뱃",20,10)
파이어뱃.공격("북동쪽")
파이어뱃.공격받음(7)
파이어뱃.공격받음(7)
파이어뱃.공격받음(7)

# 파이어뱃유닛이 북동쪽방향으로 10공격력으로 공격합니다.
# 파이어뱃이 7의 데미지를 받았습니다.
# 파이어뱃의 현재 체력은13입니다.
# 파이어뱃이 7의 데미지를 받았습니다.
# 파이어뱃의 현재 체력은6입니다.
# 파이어뱃이 7의 데미지를 받았습니다.
# 파이어뱃의 현재 체력은-1입니다.
# 파이어뱃가 살해/파괴 되었습니다.