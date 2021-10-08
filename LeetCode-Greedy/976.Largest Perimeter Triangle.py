# 삼각형을 형성하기 위한 조건 : 가장 긴 선분의 길이 < 남은 두 선분의 길이의 합
# 이 문제는 왜 그리디일까?
# 가장 큰 선분 index 를 1 이라 했을 때 2 와 3 의 합이 1보다 작다면 뒤에 선분은 비교할 필요가 없다.
# list Slicing 을 잘 활용했다고 생각한 풀이.
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        for index, _ in enumerate(nums):
            max_value = nums[index]
            if max_value < sum(nums[index + 1: index + 3]):
                return max_value + sum(nums[index + 1: index + 3])
        return 0