class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        n = len(piles) 
        piles.sort()
        # sorted_piles = sorted_piles[::-1]
        max_coin = 0
        split_round = n // 3
        for i in piles[split_round: n :2]:
            
            max_coin += i

        return max_coin

        