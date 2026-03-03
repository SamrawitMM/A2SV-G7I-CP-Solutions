class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)), reverse=True)
        n = len(sorted_nums)

        if n < 3:
            return sorted_nums[0]

        return sorted_nums[2]
        

    
        