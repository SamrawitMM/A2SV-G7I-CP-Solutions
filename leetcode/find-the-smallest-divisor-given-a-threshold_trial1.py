class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left =1
        right = max(nums)

        def check(divisor):
            
            total_sum = 0
            for n in nums:

                total_sum += ceil(n / divisor)

            # large divisor
            return total_sum <= threshold




        while left < right:

            mid = ( left + right ) // 2

            if check(mid):
                right = mid

            else:
                left = mid + 1

        
        return left




        