from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()

        n = len(nums)
        answer = 0
        left = 0
        for i in range(n):
            while min_q and min_q[-1] > nums[i]:
                min_q.pop()
            min_q.append(nums[i])
            while max_q and max_q[-1] < nums[i]:
                max_q.pop()
            
            max_q.append(nums[i])

            while abs(min_q[0] - max_q[0]) > limit:
                if min_q[0] == nums[left]:
                    min_q.popleft()

                if max_q[0] == nums[left]:
                    max_q.popleft()

                left += 1

            
            answer = max(answer, i - left + 1)

        return answer


                
                
                


            

            
        
        
            
            

      
            
                
            
            



        
