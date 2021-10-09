class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        bottom, top = 0, len(s)
        answer = []
        for character in s:
            if character == 'I':
                answer.append(bottom)
                bottom += 1
            else:
                answer.append(top)
                top -= 1
        
        return answer + [top]
        
        
        
        
        
        
        