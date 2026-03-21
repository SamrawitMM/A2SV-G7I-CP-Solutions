class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        remainders = {0: -1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remain = prefix_sum % k
            if remain in remainders:
                if i - remainders[remain] >= 2:
                    return True
            else:
                remainders[remain] = i

        return False
