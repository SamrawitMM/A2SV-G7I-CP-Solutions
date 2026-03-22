class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        window = [s[0]]
        pair = 0
        max_len = 1
        left = 0
        for i in range(1, len(s)):
            
            if s[i] == s[i-1]:
                pair += 1

            window.append(s[i])
            while left + 1 < len(s) and pair > 1 :
                if window[left] == window[left+1]:
                    pair -= 1

                
                left += 1
                
            max_len = max(max_len, i - left + 1)

        return max_len


            





        