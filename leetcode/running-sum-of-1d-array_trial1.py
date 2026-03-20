class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            output.append(sum)

        return output
