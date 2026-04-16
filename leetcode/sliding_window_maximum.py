from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        left = 0
        for i in range(len(nums)):

            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)


            if window[0] < left:
                window.popleft()
            
            if i - left + 1 >= k:
                res.append(nums[window[0]])
                left += 1

            


        return res

            

            



        # window = deque()
        # window.extend(nums[:k])
        # res = []
        # res.append(max(window))

        # for i in range(k, len(nums)):
        #     window.append(nums[i])
        #     # while len(window) > k:
        #     window.popleft()
            
        #     if len(window) == k:
        #         res.append(max(window))


        # return res

            

        
