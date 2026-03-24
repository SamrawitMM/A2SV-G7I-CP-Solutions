class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        left = 0
        size = sum(target.values())
        output = []
        window = {}
        # for r in range(len(s)):
        #     anagram = Counter(s[r:r+size])

        #     if anagram == target:
        #         output.append(r)
            
        
        # return output

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0)  + 1

            while r - left + 1 > size:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1


            if window == target:
                output.append(left)

        return output



            
        