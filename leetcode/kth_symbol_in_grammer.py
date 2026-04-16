class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def recur(level, k, ans):

            if level == 1:
                return ans

            if k % 2 == 1:
                return recur(level-1, (k + 1)// 2, ans)

            return recur(level-1, k  // 2, 1 - ans)
    
        return recur(n, k, 0)
