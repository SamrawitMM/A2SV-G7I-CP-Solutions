class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            prev_start = result[-1][0]
            prev_end = result[-1][1]

            if cur_start <= prev_end:
                result[-1][1] = max(prev_end, cur_end)

            else:
                result.append(intervals[i])

        return result
                



        