
def solve(p):
     print("다람쥐")
     pass

# problem
p = [[0,1,0,9,0,0,0,8,7], 
     [0,0,0,2,0,0,0,0,6],
     [0,0,0,0,0,3,2,1,0],
     [0,0,1,0,4,5,0,0,0],
     [0,0,2,1,0,8,9,0,0],
     [0,0,0,3,2,0,6,0,0],
     [0,9,3,8,0,0,0,0,0],
     [7,0,0,0,0,1,0,0,0],
     [5,8,0,0,0,6,0,9,0]]

# col = column
col = [[0 for i in range(9)] for i in range(9)]

# b = box (3*3)
b = [[] for i in range(9)]

# 답 변경 체크, 더 이상 바뀐 게 없다면 2단계 진헹
blank_n=0

# 각각 비교를 위한 분류작업
for i in range(9):
     for j in range(9):
          if p[i][j]==0:
               blank_n+=1
          # column
          col[j][i]=p[i][j]
          # box # 도토리 ㅎ;
          b[i//3*3 + j//3].append(p[i][j])
          # if i<=2 and j<=2:
          #     b[0].append(p[i][j])
          # elif i<=2 and j<=5:
          #     b[1].append(p[i][j])
          # elif i<=2 and j<9:
          #     b[2].append(p[i][j])
  
          # if 2<i<=5 and j<=2:
          #     b[3].append(p[i][j])
          # elif 2<i<=5 and j<=5:
          #     b[4].append(p[i][j])
          # elif 2<i<=5 and j<9:
          #     b[5].append(p[i][j])
  
          # if 5<i<9 and j<=2:
          #     b[6].append(p[i][j])
          # elif 5<i<9 and j<=5:
          #     b[7].append(p[i][j])
          # elif 5<i<9 and j<9:
          #     b[8].append(p[i][j])

# 2. 문제 풀기

#   1) 바로 풀 수 있으면 다 풀기
#   - set 활용 (- 차집합)
s1 = set([1,2,3,4,5,6,7,8,9])
cccc=400
# 변경이 있는지 비교할 숫자
compare_n=0
while cccc>0:
     # 변경이 없다면 중단
     if compare_n==blank_n:
          break
     print(compare_n)
     compare_n=blank_n
     for i in range(9):
          for j in range(9):
               if p[i][j]==0:
                    # i에 따른 box 체크
                    n=(i//3+1)*3
                    # 1개만 추출된 경우 답
                    if len(s1-set(p[i])-set(b[j//n])-set(col[j]))==1:
                         p[i][j]=list(s1-set(p[i])-set(b[j//n])-set(col[j]))[0]
                         blank_n-=1 # 빈 곳이 채워지면 빼기
                         print(blank_n)
     cccc-=1
     print("ccccheck", cccc)
# 중간에 멈춤.. 다른 방법?




print(p)