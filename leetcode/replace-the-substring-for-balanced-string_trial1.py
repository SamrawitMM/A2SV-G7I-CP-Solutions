class Solution:
    def balancedString(self, s: str) -> int:
        valid = ['Q', 'W', 'E', 'R']
        window = Counter(s)
        left = 0
        right = 0
        threshold = len(s) // 4
        min_length = len(s)
        while right < len(s):
            window[s[right]] -= 1

            while (left < len(s) and window['Q'] <= threshold and
                  window['W'] <= threshold and
                  window['E'] <= threshold and
                  window['R'] <= threshold) :


                min_length = min(min_length, right - left + 1)

                window[s[left]] += 1
                # if window[s[left]] == 0:
                #     del window[s[left]]
                left += 1

            right += 1

        return min_length


            
