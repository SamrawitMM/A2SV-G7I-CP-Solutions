class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        i = 0
        left = 0
        n = len(cardPoints)
        ans = 0
        total_pts = sum(cardPoints)
        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum
        
        if k == n:
            return total_pts
        
        for i in range(window_size, n):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i - window_size]
            min_window = min(min_window, window_sum)

        
        return total_pts - min_window

            

        