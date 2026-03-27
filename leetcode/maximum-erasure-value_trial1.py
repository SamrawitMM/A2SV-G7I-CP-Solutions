class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = defaultdict(int)
        window_sum = 0
        max_sum = 0
        left = 0
        right = 0

        while right < len(nums):
            window[nums[right]] += 1

            window_sum += nums[right]

            while left < len(nums)  and window[nums[right]] >= 2:
                window[nums[left]] -= 1
                window_sum -= nums[left]

                if window[nums[left]] == 0:
                    del window[nums[left]]

                left += 1

            max_sum = max(window_sum, max_sum)

            right += 1

        return max_sum


                


        