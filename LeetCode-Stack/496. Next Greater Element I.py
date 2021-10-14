# 220ms
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for value in nums1:
            i = nums2.index(value)
            if any(value < a for a in nums2[i+1:]):
                ans.append([num for num in nums2[i+1:] if num > value][0])
            else:
                ans.append(-1)
        return ans 


# 44ms
# dictionary 로 nums2 에 대한 결과를 저장
# nums2 를 순회
# mp 의 dic : 본인의 값, value: 본인보다 처음으로 큰 값
# lambda 를 통해서 nums1 의 값을 key 로 해서 mp 에서 조회
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for idx, value in enumerate(nums2):
            dic[value] = -1
            for j in range(idx + 1, len(nums2)):
                if value < nums2[j]:
                    dic[value] = nums2[j]
                    break
        
        ans = list(map(lambda x : dic[x], nums1))
        return ans        


# 99ms
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        stack.append(nums2[0])
        
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
            
        for element in stack:
            mapping[element] = -1
        
        ans = list(map(lambda x : mapping[x], nums1))
        return ans
# Basically the problem says, if in nums1 we are working on 4, 
# then in nums2 first find where is 4 and from that index find the next number greater than 4 in nums2. 
# We can see that the solution is always coming from the reverse side of the list nums2. This should tell us to use stack.
