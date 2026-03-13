class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0

        output = []
        while i < len(firstList) and j < len(secondList):
            first_start = firstList[i][0]
            first_end = firstList[i][1]

            second_start = secondList[j][0]
            second_end = secondList[j][1]

            print(second_start, first_end)
            
            start_interval, end_interval = max(second_start, first_start), min(second_end, first_end)
            if second_start <= first_end and start_interval <= end_interval:
                output.append([max(second_start, first_start), min(second_end, first_end)])
            
            if first_end < second_end:
                i += 1
            
            else:
                j += 1

          

        return output







        