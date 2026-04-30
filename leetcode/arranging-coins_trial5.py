class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n


        def check(k):
            result = k * ( k + 1) // 2 
            return result

        while left < right:

            mid = ( left + right + 1 ) // 2

            if check(mid) > n:
                right = mid - 1

            else:
                left = mid


        return left 
        