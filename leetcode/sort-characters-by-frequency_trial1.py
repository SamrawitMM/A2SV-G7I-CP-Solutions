from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_s = sorted(freq, key = lambda x : (-freq[x], x))
        
        output = []
        for char in sorted_s:
            output.extend([char] * freq[char])

        return "".join(output)





        