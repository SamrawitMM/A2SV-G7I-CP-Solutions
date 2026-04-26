# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # left = 1
        # right = n - 1


        # while left <= right:
        #     mid_point = (left + right) // 2

        #     if isBadVersion(mid_point) != True:
        #         left = mid_point + 1

        #     else:
        #         right = mid_point - 1

        # return left

        left = 1
        right = n

        while left < right:
            mid = ( left + right ) // 2

            if isBadVersion(mid):
                right = mid
            
            else:
                left = mid + 1

        return left
      
        

        

        