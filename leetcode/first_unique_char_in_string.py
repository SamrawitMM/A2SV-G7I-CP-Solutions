from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = Counter(s)

        for key, freq in dic.items():
            if freq == 1:
                return s.index(key)

        return -1
