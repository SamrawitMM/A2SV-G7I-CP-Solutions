class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        longest = 0
        for r in range(len(s)):

            # invalid case
            while s[r] in seen:
                seen.remove(s[left])
                left += 1

            
            seen.add(s[r])
            window_size = r - left + 1
            longest = max(longest, window_size)

        return longest
