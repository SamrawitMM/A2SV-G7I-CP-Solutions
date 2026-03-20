class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        recolor = 0
        res = k

        left = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                recolor += 1

            if r - left + 1 == k:
                res = min(res, recolor)

                if blocks[left] == 'W':
                    recolor -= 1

                left += 1

        return res

            
            
        