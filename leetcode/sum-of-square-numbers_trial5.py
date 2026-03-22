class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left = 0
        # square root of c 
        right = int(c ** 0.5)

        while left <= right:
            square = left ** 2 + right ** 2

            if square == c:
                return True
            
            elif square < c:
                left += 1

            else:
                right -= 1

        return False
































        # right = 0
        # left = int(c ** 0.5)

        # while right <= left:
        #     total = right * right + left * left

        #     if total == c:
        #         return True
        #     elif total < c:
        #         right += 1
        #     else:
        #         left -= 1

        
        # return False