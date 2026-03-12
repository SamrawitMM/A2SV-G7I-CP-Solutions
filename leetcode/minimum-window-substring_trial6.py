class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        if s == t: return t
        
        target = Counter(t)
        inx, min_count = [-1, -1], float('inf')
        target_count, temp_count = len(target), 0
        window = {}
        left = 0
        for r in range(len(s)):
            current_char = s[r]
            window[current_char] = window.get(current_char, 0) + 1
            
            # check all chars and their frequency too
            if current_char in target and window[current_char] == target[current_char]:
                temp_count += 1

            # invalid
            while temp_count == target_count:
                window_size = r -left + 1
                
                if window_size < min_count:
                    inx = [left, r]
                    min_count= window_size

                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    temp_count -= 1

                left += 1
            

        l, r = inx

        return s[l:l+min_count] if min_count != float('inf') else ''




        