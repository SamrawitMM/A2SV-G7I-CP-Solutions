class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        max_ele = max(nums)
        count = [0] * (max_ele + 1)

        for num in nums:
            count[num] += 1

        result = []
        pos = 0
        for inx, value in enumerate(count):
            for _ in range(value):
                nums[pos] = inx
                pos += 1


        for inx, value in enumerate(nums):
            if target == value:
                result.append(inx)

                

        return result
        