
def solve(p):
     print("도토리")
     pass



# # r = row
# r = []
# for i in range(9):
#      r.append({1,2,3,4,5,6,7,8,9})

# # c = column
# c = []
# for i in range(9):
#      c.append({1,2,3,4,5,6,7,8,9})


# # b = box
# # 00 01 02
# # 10 11 12
# # 20 21 22
# # b = []
# # for i in range(3):
# #      bb = []
# #      for j in range(3):
# #           bb.append({1,2,3,4,5,6,7,8,9})
# #      b.append(bb)


# # 가로, 세로, 네모 집합
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

# print("row")
# for i in r:
#      print(i)
# print()

# print("column")
# for i in c:
#      print(i)
# print()

# print("box")
# for i in b:
#      for j in i:
#           print(j)
# print()