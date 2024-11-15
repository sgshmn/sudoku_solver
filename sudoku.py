print("감자")


# 1. 스도쿠 문제 입력
# p = problem
p = [[0,2,0,0,9,0,8,1,0],
     [3,0,0,8,0,0,9,6,2],
     [0,0,0,2,0,0,0,3,7],
     [0,0,0,7,0,6,0,9,0],
     [1,0,0,0,0,0,7,4,0],
     [4,0,0,1,2,3,0,0,8],
     [0,1,3,4,7,0,5,0,0],
     [0,0,7,0,5,0,3,0,0],
     [2,5,4,6,0,8,1,7,0]]


# 2. 문제 풀기

#   1) 바로 풀 수 있으면 다 풀기
# test

# r = row
r = []
for i in range(9):
     r.append({1,2,3,4,5,6,7,8,9})

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