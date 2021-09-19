# words[p] in words[:p]: 같은 문자가 있는지 조회하는 방법, list slicing 을 활용
def solution(n, words):
    for i, word in enumerate(words):
        if i != 0:
            if (words.index(word) != i) or (word[0] != words[i-1][-1]) or (len(word) < 2):
                return [(i % n) + 1, i// n + 1]   
        else:
            if len(word) < 2:
                return [1, 1]
        
    return [0, 0]