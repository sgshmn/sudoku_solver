
def solve(p):
    print("다람쥐")
    pass


class CheckNumber:    # 클래스     
    def __init__(self, p):     
        self.p = p
        self.blank_n = 0 # 빈 숫자 개수
        # col = column
        self.col = [[0 for i in range(9)] for i in range(9)]
        # b = box (3*3)
        # 0 1 2
        # 3 4 5
        # 6 7 8
        self.b = [[] for i in range(9)]
        # 들어갈 수 있는 수
        self.possible_n = [[[] for i in range(9)] for i in range(9)]
      
    # 비교를 위한 분류작업, p, col, box
    def devide(self):
        print("Devide")
        s1 = set([1,2,3,4,5,6,7,8,9])
        for i in range(9):
            for j in range(9):
                # 빈 공간 체크
                if self.p[i][j]==0:
                   self.blank_n+=1
                # column
                self.col[j][i]=self.p[i][j]
                # box # 도토리 ㅎ;
                self.b[i//3*3 + j//3].append(self.p[i][j])
        # 들어갈 수 있는 수
        for i in range(9):
            for j in range(9):
                if self.p[i][j]==0:
                    # 1개만 추출된 경우 답
                    s2=s1-set(self.p[i])-set(self.b[i//3*3 + j//3])-set(self.col[j])
                    self.possible_n[i][j]=(list(s2))    
    # 2. 문제 풀기
    #   1) 바로 풀 수 있으면 다 풀기
    #   - set 활용 (- 차집합)
    def solvee(self):
        print("Solve")
        s1 = set([1,2,3,4,5,6,7,8,9])
        # 변경이 있는지 비교할 숫자
        compare_n=0
        # 1차 진행
        # 안전핀
        cccc=100
        while cccc>0:
            # 변경이 없다면 중단
            if compare_n==self.blank_n:
                # 임의의 수 체크
                break
            compare_n=self.blank_n
            for i in range(9):
                for j in range(9):
                    if self.p[i][j]==0:
                        # 1개만 추출된 경우 답
                        s2 = s1-set(self.p[i])-set(self.b[i//3*3 + j//3])-set(self.col[j])
                        self.possible_n[i][j]=(list(s2))
                        if len(s2)==1:
                            self.p[i][j]=list(s2)[0]
                            self.col[j][i]=self.p[i][j]
                            self.b[i//3*3 + j//3].append(self.p[i][j])
                            self.blank_n-=1 # 빈 곳이 채워지면 빼기
                    else:
                        self.possible_n[i][j]=[self.p[i][j]]
            cccc-=1
            print("last----check", self.blank_n)
            if checkList(self.p, self.col, self.b, self.possible_n) < 0:
                print
                break


        









    def printP(self):
        print(f'check blank : {self.blank_n}')
        for row in self.possible_n:
        # for row in self.possible_n:
            print(row)

#   - 가능한 수의 집합(possible_n)에서 수 n 하나씩 대입
#   - 불가능(모순 발생 시) 하면 n 제거, 되돌리기(p->devide, blank_n)
#       list: [[n, blank_n, p],[n, blank_n, p],..[]]
#       모순 : 동일 가능 수 중복
def checkList(pro, col, box, pos):
    print("CheckLsit")
    c_row = [[0 for i in range(9)] for i in range(9)]
    c_col = [[0 for i in range(9)] for i in range(9)]
    c_box = [[0 for i in range(9)] for i in range(9)]
    s1 = set([1,2,3,4,5,6,7,8,9])
    for i in range(9):
        for j in range(9):
            if len(pos[i][j])==0:
                print("None")
                return -1
            if j+1 in pro[i]:
                c_row[i][j] += 1
            # column
            if j+1 in col[i]:
                c_col[i][j] += 1
            # box # 도토리 ㅎ;
            if j+1 in box[i]:
                c_box[i][j] += 1
    for i in range(9):
        if 2 in c_row[i] or 2 in c_col[i] or 2 in c_box[i]:
            print("모순발생")
            return -1
        else:
            print("문제 없음")
            return 1