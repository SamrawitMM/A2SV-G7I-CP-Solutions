class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a', 'e', 'i', 'o', 'u']
        vowel = 0
        window = defaultdict(int)
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] in v:
                vowel += 1
            window[s[i]] += 1

            while i - left + 1 > k:
                if s[left] in v:
                    vowel -= 1

                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]       
            

                left += 1

            res = max(res, vowel)

        
        return res

            







        