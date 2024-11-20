# 도토리 해법

# 2. 문제 풀기

#   1) 바로 풀 수 있으면 다 풀기
#   2) 바로 풀 수 없으면 하나씩 대입
#   3) 모순을 발견하면 가장 최근에 대입했던 곳으로 돌아가기(스택을 사용)

class paan:
    def __init__(self, p):
        # p = problem
        self.p = p
        # r = row
        self.r = []
        for i in range(9):
            self.r.append({1,2,3,4,5,6,7,8,9})

        # c = column
        self.c = []
        for i in range(9):
            self.c.append({1,2,3,4,5,6,7,8,9})

        # b = box
        # 00 01 02
        # 10 11 12
        # 20 21 22
        self.b = []
        for i in range(3):
            bb = []
            for j in range(3):
                bb.append({1,2,3,4,5,6,7,8,9})
            self.b.append(bb)

     


# 가로, 세로, 네모 집합
for i in range(9):
    for j in range(9):
          x = p[i][j]
          if x != 0:
               r[i].discard(x)
               c[j].discard(x)
               b[i//3][j//3].discard(x)




# 1. 스도쿠 문제 입력
# p = problem
def solve(p):
    print("도토리")