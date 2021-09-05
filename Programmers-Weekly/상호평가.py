scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
reverse_scores = [[row[i] for row in scores] for i in range(len(scores))]
average_list = []
answer = ''

for row_i, row in enumerate(reverse_scores):
    if row[row_i] == max(row) or row[row_i] == min(row):
        average = (sum(row) - row[row_i]) / (len(scores) - 1)
    else:
        average = sum(row) / len(scores)
    average_list.append(average)

for average in average_list:
    if average >= 90:
        answer += 'A'
    elif 80 <= average < 90:
        answer += 'B'
    elif 70 <= average < 80:
        answer += 'C'
    elif 50 <= average < 70:
        answer += 'D'
    elif average < 50:
        answer += 'F'

print(answer)

# "CFD"
# 평균	학점
# 90점 이상	A
# 80점 이상 90점 미만	B
# 70점 이상 80점 미만	C
# 50점 이상 70점 미만	D
# 50점 미만	F