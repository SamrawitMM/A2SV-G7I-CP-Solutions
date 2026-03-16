class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_sum = sum(nums[:k])
        maximum = max_sum

        for i in range(k, len(nums)):

            max_sum += nums[i]
            max_sum -= nums[i-k]

            maximum = max(max_sum, maximum)

        return maximum / k











        # max_sum = sum(nums[:k])
        # maxim = max_sum
        
        
        # for i in range(k, len(nums)):

        #     max_sum += nums[i]
        #     max_sum -= nums[i-k]

        #     maxim = max_sum if max_sum > maxim else maxim


        # return maxim / k




