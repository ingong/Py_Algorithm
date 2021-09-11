# valid 를 통해서 유효한 범위 내인지를 확인
# check 함수를 통해 거리두기를 지키고 있는 지 여부확인
def solution(places):
    answer = []
    
    size = 5
    def valid(r, c):
        return -1<r<size and -1<c<size
    
    def check(x, y, place):
        dist = [(1,0),(0,1),(-1,0),(0,-1)]
        for dx, dy in dist:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and place[nx][ny]=='P':
                return False
        
        dist = [(-1,-1),(-1,1),(1,-1),(1,1)]
        for dx, dy in dist:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and place[nx][ny]=='P' and (place[x][ny]!='X' or place[nx][y]!='X'):
                return False
        
        dist = [(2,0), (0,2), (-2,0), (0,-2)]
        for dx, dy in dist:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and place[nx][ny] =='P' and place[x+dx//2][y+dy//2] !='X':
                return False
        return True
    
    for place in places:
        flag = False
        for r, c in [(i, j) for i in range(5) for j in range(5)]:
            if place[r][c] == 'P':
                result = check(r,c, place)
                if not result:
                    answer.append(0)
                    flag = True
                    break
        if not flag:
            answer.append(1)
        
    return answer