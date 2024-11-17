print("감자")


# 1. 스도쿠 문제 입력
# p = problem
# p = [[0,2,0,0,9,0,8,1,0],
#      [3,0,0,8,0,0,9,6,2],
#      [0,0,0,2,0,0,0,3,7],
#      [0,0,0,7,0,6,0,9,0],
#      [1,0,0,0,0,0,7,4,0],
#      [4,0,0,1,2,3,0,0,8],
#      [0,1,3,4,7,0,5,0,0],
#      [0,0,7,0,5,0,3,0,0],
#      [2,5,4,6,0,8,1,7,0]]

# problem and answer
p=[[0,1,0,9,0,0,0,8,7], 
   [0,0,0,2,0,0,0,0,6],
   [0,0,0,0,0,3,2,1,0],
   [0,0,1,0,4,5,0,0,0],
   [0,0,2,1,0,8,9,0,0],
   [0,0,0,3,2,0,6,0,0],
   [0,9,3,8,0,0,0,0,0],
   [7,0,0,0,0,1,0,0,0],
   [5,8,0,0,0,6,0,9,0]]

# a =[[2, 1, 5, 9, 6, 4, 3, 8, 7], 
#     [8, 3, 9, 2, 1, 7, 4, 5, 6], 
#     [6, 4, 7, 5, 8, 3, 2, 1, 9], 
#     [9, 7, 1, 6, 4, 5, 8, 2, 3], 
#     [3, 6, 2, 1, 7, 8, 9, 4, 5], 
#     [4, 5, 8, 3, 2, 9, 6, 7, 1], 
#     [1, 9, 3, 8, 5, 2, 7, 6, 4], 
#     [7, 2, 6, 4, 9, 1, 5, 3, 8], 
#     [5, 8, 4, 7, 3, 6, 1, 9, 2]]

# col = column
col = [[0 for i in range(9)] for i in range(9)]

# b = box (3*3)
b = [[] for i in range(9)]

# 각각 비교를 위한 분류작업
for i in range(9):
    for j in range(9):
        # column
        col[j][i]=p[i][j]
        # box
        if i<=2 and j<=2:
            b[0].append(p[i][j])
        elif i<=2 and j<=5:
            b[1].append(p[i][j])
        elif i<=2 and j<9:
            b[2].append(p[i][j])

        if 2<i<=5 and j<=2:
            b[3].append(p[i][j])
        elif 2<i<=5 and j<=5:
            b[4].append(p[i][j])
        elif 2<i<=5 and j<9:
            b[5].append(p[i][j])

        if 5<i<9 and j<=2:
            b[6].append(p[i][j])
        elif 5<i<9 and j<=5:
            b[7].append(p[i][j])
        elif 5<i<9 and j<9:
            b[8].append(p[i][j])


# 2. 문제 풀기

#   1) 바로 풀 수 있으면 다 풀기
#   - set 활용 (- 차집합)
s1 = set([1,2,3,4,5,6,7,8,9])

for i in range(9):
    for j in range(9):
        if p[i][j]==0:
            check1 = 0
            if i<=2:
                check1=3
            elif i<=5:
                check1=6
            else:
                check1=9
            # 1개만 추출된 경우 답
            if len(s1-set(p[i])-set(b[j//check1])-set(col[j]))==1:
                p[i][j]=list(s1-set(p[i])-set(b[j//check1])-set(col[j]))[0]

print(p)

# 여러번 돌린 결과
# p = [[7, 2, 6, 3, 9, 4, 8, 1, 5], 
#      [3, 4, 5, 8, 1, 7, 9, 6, 2], 
#      [8, 9, 1, 2, 6, 5, 4, 3, 7], 
#      [5, 3, 8, 7, 4, 6, 2, 9, 1], 
#      [1, 6, 2, 5, 8, 9, 7, 4, 3], 
#      [4, 7, 9, 1, 2, 3, 6, 5, 8], 
#      [9, 1, 3, 4, 7, 2, 5, 8, 6], 
#      [6, 8, 7, 9, 5, 1, 3, 2, 4], 
#      [2, 5, 4, 6, 3, 8, 1, 7, 9]]

# <<<<<<< main
# =======
# # r = row
# r = []
# for i in range(9):
#      r.append({1,2,3,4,5,6,7,8,9})
# >>>>>>> main

# c = column
c = []
for i in range(9):
     c.append({1,2,3,4,5,6,7,8,9})

# b = box
# 00 01 02
# 10 11 12
# 20 21 22
b = []
for i in range(3):
     bb = []
     for j in range(3):
          bb.append({1,2,3,4,5,6,7,8,9})
     b.append(bb)


for i in range(9):
    for j in range(9):
          x = p[i][j]
          if x != 0:
               r[i].discard(x)
               c[j].discard(x)
               b[i//3][j//3].discard(x)

print("problem")
for i in p:
     print(i)
print()

print("row")
for i in r:
     print(i)
print()

print("column")
for i in c:
     print(i)
print()

print("box")
for i in b:
     for j in i:
          print(j)
print()

#   2) 바로 풀 수 없으면 하나씩 대입
#   3) 모순을 발견하면 가장 최근에 대입했던 곳으로 돌아가기(스택을 사용)


# 3. 푼 결과 출력