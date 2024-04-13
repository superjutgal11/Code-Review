# a = [[1,2,3,4],[5,6,7,8],[9, 10, 11, 12],[13, 14, 15, 16]]

# b = [[0]*len(a) for i in range(len(a))]

# for i in range(len(a)):
#     for j in range(len(a)):
#         b[j][len(a)-i-1] = a[i][j]
# print(b)


# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# n, m = len(lock), len(key)

# new_lock = [[0]*3*n for i in range(3*n)] # 자물쇠의 3배 크기의 영행렬
# for i in range(n):
#     for j in range(n):
#         new_lock[n+i][n+j] = lock[i][j];
# # new_lock의 중앙 부분에 자물쇠의 값이 들어가버림!!!

# ans = False

# for x in range(4): # 90도씩 돌리는 경우
#     for i in range(2*n - m): # 3n크기의 범위에 대입하는 x축
#         for j in range(2*n - m): # 3n크기의 범위에 대입하는 y축
#             for i_2 in range(m): # 키의 행을 넣음
#                 for j_2 in range(m): # 키의 열을 넣음
#                     new_lock[i][j] = key[n+i_2][n+j_2] + new_lock[n+i_2][n+j_2]
#             for i_3 in range(n):
#                 for j_3 in range(n):
#                     if(new_lock[n+i_3][n+j_3] != 1):
#                         ans = False
#                     else:
#                         ans = True
                
# print(ans)


def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] not in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(num[i])
            clean_num.append(num[i])
            
    # 아래 코드에는 틀린 부분이 없습니다.
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer