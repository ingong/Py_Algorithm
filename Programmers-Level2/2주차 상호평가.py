# 유일한 점수라는 조건을 확인하지 않고, 풀어서 edge 케이스에서 실패
# 문제를 다시 읽어보고 유일한 조건을 확인했고, 통과함
# ?새로알게 된 내용
# 1. calculate 함수 외에 다른 좋은 방법이 있음
# 2차원 배열을 뒤집는 좋은 방법
# list(mpa(list, zip(*scores)))
# 2. calculate 함수를 사용하지 않아도됨 
# return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])
# 3. 해당 열에서 유일한 값인지를 확인하는 방법
# 해당 열에서 본인의 숫자를 count 하고 이 값이 1 인지를 확인하면됨
# 굳이 in 을 사용하지 않아도 될듯
def calculate(score):
    if 90 <= score:
        return 'A'
    elif 80 <= score and score < 90:
        return 'B'
    elif 70 <= score and score < 80:
        return 'C'
    elif 50 <= score and score < 70:
        return 'D'
    elif score < 50:
        return 'F'
    
def solution(scores):
    answer = []
    n = len(scores)
    # reversed_scores = list(map(list, zip(*scores)))
    reversed_scores = [[row[i] for row in scores] for i in range(n)] 
    for index, score in enumerate(reversed_scores):
        if score[index] == max(score) and not score[index] in (score[:index] + score[index+1:]):
            answer.append((sum(score) - score[index]) / (n - 1))
        elif score[index] == min(score) and not score[index] in (score[:index] + score[index+1:]):
            answer.append((sum(score) - score[index]) / (n - 1))
        else:
            answer.append(sum(score)/n)
    
    answer = list(map(calculate, answer))
    return ''.join(answer)