class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        
        i = 0
        placement = [0] * len(score)
        sorted_score = sorted(score, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
        dict = {}
        for inx, num in enumerate(sorted_score):
            if inx == 0:
                dict[num] = rank[inx]
            elif inx == 1:
                dict[num] = rank[inx]
            elif inx == 2:
                dict[num] = rank[inx]
            else:
                dict[num] = str(inx + 1)
  
        while i < len(score):
            placement[i] = dict[score[i]]
            i += 1
        
        return placement
            

            


