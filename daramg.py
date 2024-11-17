
def solve(p):
     print("다람쥐")
     pass

# # col = column
# col = [[0 for i in range(9)] for i in range(9)]

# # b = box (3*3)
# box = [[] for i in range(9)]

# # 각각 비교를 위한 분류작업
# for i in range(9):
#     for j in range(9):
#         # column
#         col[j][i]=p[i][j]
#         # box

#         if i<=2 and j<=2:
#             box[0].append(p[i][j])
#         elif i<=2 and j<=5:
#             box[1].append(p[i][j])
#         elif i<=2 and j<9:
#             box[2].append(p[i][j])

#         if 2<i<=5 and j<=2:
#             box[3].append(p[i][j])
#         elif 2<i<=5 and j<=5:
#             box[4].append(p[i][j])
#         elif 2<i<=5 and j<9:
#             box[5].append(p[i][j])

#         if 5<i<9 and j<=2:
#             box[6].append(p[i][j])
#         elif 5<i<9 and j<=5:
#             box[7].append(p[i][j])
#         elif 5<i<9 and j<9:
#             box[8].append(p[i][j])


# # 2. 문제 풀기

# #   1) 바로 풀 수 있으면 다 풀기
# #   - set 활용 (- 차집합)


# #   - set 활용 (- 차집합)
# s1 = set([1,2,3,4,5,6,7,8,9])


# for i in range(9):
#     for j in range(9):
#         if p[i][j]==0:
#             check1 = 0
#             if i<=2:
#                 check1=3
#             elif i<=5:
#                 check1=6
#             else:
#                 check1=9
#             # 1개만 추출된 경우 답
#             if len(s1-set(p[i])-set(b[j//check1])-set(col[j]))==1:
#                 p[i][j]=list(s1-set(p[i])-set(box[j//check1])-set(col[j]))[0]

# # 전 문제를 저장, 바뀐 게 없다면 2단계 진헹
# exP = p

# print(p)

# # 가로, 세로, 네모에 가능한 수를 집합으로 만든다