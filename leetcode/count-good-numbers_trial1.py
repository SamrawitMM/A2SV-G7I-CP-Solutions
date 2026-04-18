class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, n):
            if n == 0:
                return 1

            res = 1
            while n > 1:

                if n % 2 :
                    res = ( res * x ) % MOD

                n = n // 2
                x = ( x * x ) % MOD

            return res * x


        total_even_num = ceil(n/2)
        total_odd_num = n // 2

        return (power(5, total_even_num) * power(4, total_odd_num))   % MOD

        

        


        