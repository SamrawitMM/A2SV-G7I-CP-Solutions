class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        window = defaultdict(int)
        left = 0
        count = 0
        for i in range(len(fruits)):

            window[fruits[i]] += 1

            while len(window) > 2 and left < len(fruits):
                window[fruits[left]] -= 1

                if window[fruits[left]] == 0:
                    del window[fruits[left]]

                left += 1

            count = max(count, i - left + 1)

        return count

            


        