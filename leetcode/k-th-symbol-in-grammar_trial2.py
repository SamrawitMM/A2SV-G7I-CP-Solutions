class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def recur2(level, k):

            total_length = 2 ** (level-1)
            mid_point = total_length // 2

            if level == 1:
                return 0

            if k <= mid_point:
                return recur2(level-1, k)

            else:
                print(k, mid_point)
                prev_char = recur2(level-1, k - mid_point)
                return 1 - prev_char


        # def recur(level, k, ans):

        #     if level == 1:
        #         return ans

        #     if k % 2 == 1:
        #         return recur(level-1, (k + 1)// 2, ans)

        #     return recur(level-1, k  // 2, 1 - ans)
    
        return recur2(level= n, k = k)