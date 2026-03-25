class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        count = 0

        start, end = 0, 0
        for i in range(len(nums)):
            
            if nums[i] % 2:
                odd += 1

            
            while odd > k:

                if nums[start] % 2:
                    odd -= 1

                    start += 1
                    end = start


            if odd == k:
                while not nums[end] % 2:
                    end += 1

                count += end - start + 1


        return count

                


        