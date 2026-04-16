class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power_four(n):
            if n == 1:
                return True
            
            if n < 1:
                return False

            return power_four(n / 4)

        return power_four(n)
        
