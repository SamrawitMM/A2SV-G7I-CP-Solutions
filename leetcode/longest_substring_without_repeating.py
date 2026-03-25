class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        count = 0
        left = 0
        for i in range(len(s)):
            window[s[i]] += 1
            
            while window[s[i]] > 1:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            count = max(count, i - left + 1)

        return count
