class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums_sorted = sorted(set(nums))
        included = 0
        j = 0
        for i in range(len(nums_sorted)):
            # included range
            while j < len(nums_sorted) and nums_sorted[j] <= nums_sorted[i] + n -1 :
                j += 1

            included = max(included, j - i)


            

        return n - included
        