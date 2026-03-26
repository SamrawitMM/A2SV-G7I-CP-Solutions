class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        window_sum = 0
        max_distinct_sum = 0
        for i in range(k):
            window[nums[i]] += 1
            window_sum += nums[i]

            
        if len(window) == k:
            max_distinct_sum = max(max_distinct_sum, window_sum)
        
        left = 0
        right = k
        while right < len(nums):
            window[nums[right]] += 1
            window_sum += nums[right]


            window[nums[left]] -= 1
            window_sum -= nums[left]

            if window[nums[left]] == 0:
                del window[nums[left]]

            

            if len(window) == k:
                max_distinct_sum = max(max_distinct_sum, window_sum)

            # print(window)

            left += 1
            right += 1

            

        return max_distinct_sum



































        # window = {}
        # max_distinct_sum = 0
        # window_sum = 0

        # # first k sized window
        # for i in range(k):
        #     window[nums[i]] = window.get(nums[i], 0) + 1
        #     window_sum += nums[i]
        
        # # compute the sum if distinct k size in window
        # if k == len(window):
        #     max_distinct_sum = max(window_sum, max_distinct_sum)
        
        # print(max_distinct_sum)
            

        # right = k
        # left = 0

        # # compute the next k sized window
        # while right < len(nums):
        #     # print(window)
        #     window[nums[right]] = window.get(nums[right], 0) + 1
        #     window_sum += nums[right]

        #     # remove the leftmost item
        #     window[nums[left]] -= 1
        #     window_sum -= nums[left]
            
        #     # if freq is 0 remove from current window
        #     if window[nums[left]] == 0:
        #         del window[nums[left]]


        #     if len(window) == k:
        #         max_distinct_sum = max(window_sum, max_distinct_sum)

                

        #     left += 1
        #     right += 1

        # return max_distinct_sum
 

        