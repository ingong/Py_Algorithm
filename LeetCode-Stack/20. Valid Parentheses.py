class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[' : ']', '{' : '}'}
        stack = []
        for tag in s[::-1]:
            if stack and tag in list(dic.keys()):
                if dic.get(tag) != stack.pop():
                    return False 
            else:
                stack.append(tag)
                
        return True if not stack else False