# 도토리 해법

# 2. 문제 풀기

#   1) 바로 풀 수 있으면 다 풀기
#   2) 바로 풀 수 없으면 하나씩 대입
#   3) 모순을 발견하면 가장 최근에 대입했던 곳으로 돌아가기(스택을 사용)


# 스도쿠 답지 9X9판
class paan():
     def __init__(self):
          pass



# 스도쿠 스택 sudoku stack(ss) 만들기
# sudoku stack node
class ssn():
     def __init__(self, data):
          self.data = data
          self.next = None


class ss():
     def __init__(self):
          self.top = None
     
     def push(self, data):
        if self.top is None:
            self.top = ssn(data)
        else:
            node = ssn(data)
            node.next = self.top
            self.top = node

     def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

     def peek(self):
        if self.top is None:
            return None
        return self.top.data

     def is_empty(self):
        return self.top is None




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


# 가로, 세로, 네모 집합
# for i in range(9):
#     for j in range(9):
#           x = p[i][j]
#           if x != 0:
#                r[i].discard(x)
#                c[j].discard(x)
#                b[i//3][j//3].discard(x)



# print("problem")
# for i in p:
#      print(i)
# print()

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


# 1. 스도쿠 문제 입력
# p = problem
def solve(p):
     print("도토리")