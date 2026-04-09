class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        n = len(nums)
        nums_duplicate = nums * 2
        n2 = len(nums_duplicate)
        result = [-1] * n2
        for i in range(n2):
            while stack and nums_duplicate[stack[-1]] < nums_duplicate[i]:
                result[stack[-1]] = nums_duplicate[i]
                stack.pop()

            stack.append(i)

        return result[:n]


