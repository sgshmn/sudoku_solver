# 도토리 해법

# rows, colums, boxes
# 가로, 세로, 네모에서 가능한 수의 집합을 표현할 때 사용
# 왼쪽 위부터 책 읽는 방향으로 순서를 매긴다

rows = []
columns = []
boxes = []
for i in range(9):
    rows.append({1,2,3,4,5,6,7,8,9})
    columns.append({1,2,3,4,5,6,7,8,9})
    boxes.append({1,2,3,4,5,6,7,8,9})


# problem[i][j]가 있는 네모를 찾는다
def calculateBoxIndex(i, j):
    return i//3*3 + j//3

# 가로, 세로, 네모 집합에서 원소 삭제하기    
def removeElement(x, i, j):
    k = calculateBoxIndex(i, j)
    rows[i].discard(x)
    columns[j].discard(x)
    boxes[k].discard(x)

# 가로, 세로, 네모 집합 초기화
def initSets():
    for i in range(9):
        for j in range(9):
            x = problem[i][j]
            if problem[i][j] != 0:
                removeElement(x, i, j)
 

# problem[i][j]에서 가능한 수의 집합 계산
def calculatePossibleSudokuSet(i, j):
    k = calculateBoxIndex(i, j)
    return set.intersection(rows[i], columns[j], boxes[k])

def printNow():
    print("출력")
    for i in problem:
        print(i)

def fillBlanks(problem):
    # n : while문 안에서 인덱스 대용
    # c : 연속으로 바뀌지 않은 횟수
    n = 0
    c = 0

    # 변화가 있으면 c에 1을 더한다
    # 변화가 없으면 c = 0 초기화
    # 81번 연속 변화가 없으면 함수를 끝낸다
    while c < 81:
        # row, column 번호 계산
        n %= 81

        i = n // 9
        j = n % 9
        
        # 값이 0이 아니면 이미 넣은 것
        # 넘어가자 
        if problem[i][j] != 0:
            n += 1
            c += 1
            continue

        # 0이면 값을 넣어야 한다
        # 가능한 값을 찾기
        possibles = calculatePossibleSudokuSet(i, j)
        l = len(possibles)
        
        # 가능한 값이 없다면 모순
        # 가정해서 대입하기 전으로 돌아가야한다
        if l == 0:
            print("막힌 곳. 되돌아가기 아직 구현 못함")
            return 1 # 1 : 모순
        
        # 가능한 값이 1개라면 그 값이 답이다
        if l == 1:
            one = next(iter(possibles))
            problem[i][j] = one
            removeElement(one, i, j)
            n += 1
            c = 0
        
        # 가능한 값이 2개 이상이면 넘어간다
        else:
            n += 1
            c += 1
            continue

    return 0 # 더이상 변화가 없는 상태


# inputProblem은 9X9 리스트
def solve(inputProblem):
    print("도토리")

    global problem

    # 문제를 입력
    problem = inputProblem
    initSets()
    
    # 빈칸 채우기
    sign = fillBlanks(problem)
    print(sign)
    # printNow()