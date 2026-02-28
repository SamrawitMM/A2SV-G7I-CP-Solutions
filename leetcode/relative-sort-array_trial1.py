from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)

        sorted(freq)
        result = []
        
        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])

        remaining = []

        for num in arr1:
            if num not in arr2:
                remaining.append(num)

        result.extend(sorted(remaining))

        return result

        