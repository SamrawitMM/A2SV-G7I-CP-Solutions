class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power_sum(x, n):

            if n < 0:
                x = 1 / x
                n = -n

            res = 1
            while n > 0:
                if n % 2:
                    res = res * x

                n = n // 2
                x = x * x

            return res

        return power_sum(x, n)

            
        