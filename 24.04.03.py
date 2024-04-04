# 파이썬 수업 예제 풀이 연습

# 다음과 같이 출력이 되도록 이중 중첩 for문 및 중첩 없는 for문을 통해 구현하라.
'''
#
 #
  #
   #
    #
     #
      #
'''

# 이중 중첩 for문으로 구현

# n = 7

# for i in range(n):
#     st = ' '
#     for j in range(n):
#         print(st*j,end="")
#     print('#')


# def solution(n):
#     li = [] # 반대
#     anw = 0
#     while n:
#         li.append(n%3)
#         n=n//3
#     for i in range(len(li)):
#         anw = anw + 3**(len(li)-i-1) * li[i]
#     return anw

# print(solution(62))














# 최소 7 이상이여야 한다는 조건문은 and 조건으로, 3의 배수와 7의 배수는 각각 or조건으로 구상해 보았습니다.

inp_num = int(input("숫자를 하나 입력하세요 : "))

if inp_num >=7 and ( inp_num % 3 == 0 or inp_num % 7==0):
    print("{}은/는 3 또는 7의 배수입니다.".format(inp_num))
else:
    print("{}은/는 3 또는 7의 배수가 아닙니다.".format(inp_num))