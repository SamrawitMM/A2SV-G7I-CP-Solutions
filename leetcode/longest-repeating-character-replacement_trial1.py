class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        
        j = 0

        res = 0
        
        for i in range(len(s)):

            freq[s[i]] += 1
            max_freq = max(freq.values())
            current_length = i - j + 1

            if current_length - max_freq > k:
                freq[s[j]] -= 1
                j += 1

            res = max(res, i - j + 1)

        
        return res
            




        