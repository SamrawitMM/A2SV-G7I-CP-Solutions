class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        window = defaultdict(int)
        equal_pairs = 0
        good_subarray = 0
        while right < len(nums):
            equal_pairs += window[nums[right]]
            window[nums[right]] += 1

            while left < len(nums) and equal_pairs >= k:
                window[nums[left]] -= 1
                equal_pairs -= window[nums[left]]

                left += 1

            good_subarray += left
            right += 1


        return good_subarray




            

        