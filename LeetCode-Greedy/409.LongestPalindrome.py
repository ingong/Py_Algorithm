# 기존의 문제랑 비슷하다고 생각하고 접근했다가 오래 걸린문제
# 예시를 꼼꼼하게 읽어볼 필요가 있음
# 문제를 좌, 우 대칭으로 접근하는 것이 아닌 해당 문자열을 가지고 조합해서 만들 수 있는 가장 긴 문자열 문제임
# 짝수의 경우에는 answer 에 더해줌
# 홀수의 경우에는 1을 빼고 answer 에 더해주고]
# 만약 더 해진 합이 짝수라면 answer += 1 을 해주면 된다
# b b 인 상황에서 ccc 를 더하는 것이 가능하기 때문에 b c c b 로 만들고 가운데에 c 를 넣는 것이 가능하다
# 이번 차수가 홀수이고, (홀수 - 1) + answer 가 짝수라면 1 을 더해서 palindrome 을 만들 수 있다.
# 즉, 처음에 answer 에 홀수를 더해주는 경우만 가능
# 기존에 실패했던 defaultDict 를 활용한 문제에서도 odd 값을 1 씩 빼준뒤 전부다 더하고, 마지막에 1 을 더해주면 된다. 
from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        answer = 0
        for value in Counter(s).values():
            if value % 2 == 0:
                answer = answer + value
            else:
                answer = answer + (value - 1)    
            
            if answer % 2 == 0 and value % 2 == 1:
                answer += 1
        
        return answer