# 첫 번째는 문제를 제대로 읽지 않아서 접근 방법이 잘못되었고, 두 번째는 조건을 구별하지 않아서 틀림
# 두 번째 시도 후 5개의 테스크케이스와 1개의 효율성 검사에서 통과하지 못해서\
# 블로그에서 접근방법을 확인 후 풀이
# 그냥 쉽게 첫 번째 스티커를 뗄 때와 떼지 않을 때를 구별하면 됨 
# 해당 문제는 다음 주에 다시 풀어볼 예정
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    # 맨 앞 스티커를 떼는 경우
    board = [0 for _ in sticker]
    board[0] = sticker[0]
    board[1] = board[0]
    for i in range(2, len(sticker) - 1):
        board[i] = max(board[i-2] + sticker[i], board[i-1])
    answer1 = max(board)
    
    # 맨 앞 스티커를 떼지 않는 경우 (테스트 케이스는 둘다 떼지않는 경우)
    board2 = [0 for _ in sticker]
    board2[0] = 0
    board2[1] = sticker[1]
    for i in range(2, len(sticker)):
        board2[i] = max(sticker[i] + board2[i-2], board2[i-1])
    answer2 = max(board2)
    
    return max(answer1, answer2)
    # return max(dp)