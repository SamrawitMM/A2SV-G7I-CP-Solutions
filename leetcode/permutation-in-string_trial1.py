class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        right = 0
        left = 0

        window = defaultdict(int)
        freq_s1 = Counter(s1)
        while right < len(s2):
            window[s2[right]] += 1

            while left < len(s2) and right - left + 1 > len(s1):

                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            print(window)
            if freq_s1 == window:
                return True

            
            right += 1

        return False


