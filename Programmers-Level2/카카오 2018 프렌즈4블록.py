# checkList False + 본인이 '' 이 아니면서 + 좌, 우, 대각선에 있는 것들이 동일
# 블록지우기
# 이동시키기

# 오래걸린 이유
# 1. 첫번째 반복문에서 board_list 가 아니라 board 참조
# 2. rjust 함수를 사용할 때 세로를 기준으로 작성했어야했는데, 가로 기준으로 작성함
# => 2차원 배열에서 행과 열의 개념이 아직도 좀 헷갈린다. 특히 뒤집을 때 더 헷갈리는 것 같다. 반복학습이 필요하다

def isRemovable(board, row, column):
    return (board[row][column] == board[row + 1][column]) and (board[row][column] == board[row][column + 1]) and (board[row][column] == board[row + 1][column + 1])
    

def solution(m, n, board):
    board_list = [[board[row][column] for column in range(n)] for row in range(m)]
    target_list = []
    
    while True:
        for row in range(m-1):
            for column in range(n-1):
                if board_list[row][column] != ' ' and isRemovable(board_list, row, column):
                    print(board[row][column])
                    target_list.append([row, column])

        for [row, column] in target_list:
            board_list[row][column] = ''
            board_list[row + 1][column] = ''
            board_list[row][column + 1] = ''
            board_list[row + 1][column + 1] = ''

        if len(target_list) == 0:
            break

        reverse_board = [("").join([row[i] for row in board_list]).rjust(m, ' ') for i in range(n)]
        board_list = [[row[i] for row in reverse_board] for i in range(m)]
        target_list = []
        
    count = 0
    for row in board_list:
        for value in row:
            if value == ' ':
                count += 1
                
    return counta