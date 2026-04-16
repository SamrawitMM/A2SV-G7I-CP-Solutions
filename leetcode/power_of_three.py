class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        def power_three(n):
            

            if n == 1:
                return True
            if n < 1:
                return False

            return power_three(n / 3)

        return power_three(n)
        
