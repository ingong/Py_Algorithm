def solution(table, languages, preference):
    answer = {}
    for score_str in table:
        score_list = score_str.split()
        for lang, pref in zip(languages, preference):  
            if lang in score_list:
                answer[score_list[0]] = answer.get(score_list[0], 0) + (6 - score_list.index(lang)) * pref
            else:
                pass
    
    return sorted(answer.items(), key = lambda x : [-x[1], x[0]])[0][0]
  
# 새롭게 배운 내용
# 1. zip 을 통해서 접근 (기존에는 동일한 순서를 갖기 때문에 index 로 접근했는데, 바꿔보니 zip 이 더 가독성이 좋음)
# 2. 굳이 너무 많은 변수를 선언하는 것보다는 간결하게 하는 것이 좋은 것 같다.
# 3. 마지막에 정렬할 때, 한 번은 내림차순, 한 번은 오름차순이라 각각을 정렬했는데 [-x[1], x[0]] 이런 식으로 정렬하면 
# 둘 다 만족하는 정렬을 구현할 수 있음