
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
 
    def printP(self):
        print(f'check blank : {self.blank_n}')
        for row in self.p:
        # for row in self.possible_n:
            print(row)
      
    # 각각 비교를 위한 분류작업
    def devide(self):
        print("Devide")
        s1 = set([1,2,3,4,5,6,7,8,9])
        for i in range(9):
            for j in range(9):
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
                                # 가능한 수 비우기~
                                self.possible_n[i][j].clear()
            cccc-=1
            print("last----check", self.blank_n)


