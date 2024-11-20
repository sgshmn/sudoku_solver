# 도토리 해법

# 2. 문제 풀기


# 1~9가 있는 집합 9개의 리스트 생성
# 가로, 세로, 네모에서 가능한 수의 집합을 표현할 때 사용
def createThreeSudokuSetList():
    newSetList1 = []
    newSetList2 = []
    newSetList3 = []
    for i in range(9):
        newSetList1.append({1,2,3,4,5,6,7,8,9})
        newSetList2.append({1,2,3,4,5,6,7,8,9})
        newSetList3.append({1,2,3,4,5,6,7,8,9})
    return newSetList1, newSetList2, newSetList3

# row, column은 왼쪽 위부터 오른쪽 아래로 순서를 매긴다
# box는 다음과 같다
# 0 1 2
# 3 4 5
# 6 7 8

# problem[i][j]가 있는 네모를 찾는다
def calculateBoxIndex(i, j):
    return i//3*3 + j//3

class paan:
    def __init__(self, problem):
        self.problem = problem # 9X9 리스트
        self.rows, self.columns ,self.boxes = createThreeSudokuSetList()
        self.__initiateSetLists__()
        
    def __initiateSetLists__(self):
        for i in range(9):
            for j in range(9):
                x = self.problem[i][j]
                if self.problem[i][j] == 0:
                    self.removeElement(x, i, j)

    # 가로, 세로, 네모 집합에서 원소 삭제하기
    # problem의 0을 다른 숫자로 바꾸면 실행한다
    def removeElement(self, x, i, j):
        k = calculateBoxIndex(i, j)
        self.rows[i].discard(x)
        self.columns[j].discard(x)
        self.boxes[k].discard(x)
    
    # problem[i][j]에서 가능한 수의 집합 계산
    def calculatePossibleSudokuSet(self, i, j):
        k = calculateBoxIndex(i, j)
        return set.intersection(self.rows[i], self.columns[j], self.boxes[k])
    
    def printNow(self):
        print("출력")
        for i in self.problem:
            print(i)

def fillBlanks(paanX : paan):
    # n : while문 안에서 인덱스 대용
    # c : 연속으로 바뀌지 않은 횟수
    n = 0
    c = 0

    # 변화가 있으면 c에 1을 더한다
    # 변화가 없으면 c = 0 초기화
    # 81번 연속 변화가 없으면 함수를 끝낸다
    while c < 81:
        # row, column 번호 계산
        i = n // 9
        j = n % 9
        
        # 값이 0이 아니면 이미 넣은 것
        # 넘어가자 
        if paanX.problem[i][j] != 0:
            n += 1
            c += 1
            continue

        # 0이면 값을 넣어야 한다
        # 가능한 값을 찾기
        possibles = paanX.calculatePossibleSudokuSet(i, j)
        l = len(possibles)
        
        # 가능한 값이 없다면 모순
        # 가정해서 대입하기 전으로 돌아가야한다
        if l == 0:
            print("막힌 곳. 되돌아가기 아직 구현 못함")
            break
        
        # 가능한 값이 1개라면 그 값이 답이다
        if l == 1:
            paanX.problem[i][j] = possibles[0]
            paanX.removeElement(i, j)
            n += 1
            c = 0
        
        # 가능한 값이 2개 이상이면 넘어간다
        else:
            n += 1
            c += 1
            continue

    paanX.printNow()


# 1. 스도쿠 문제 입력
# problem은 9X9 리스트
def solve(problem):
    print("도토리")

    paanX = paan(problem)
    fillBlanks(paanX)