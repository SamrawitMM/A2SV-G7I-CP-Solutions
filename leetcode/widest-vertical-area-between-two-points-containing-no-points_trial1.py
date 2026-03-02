class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_length  = 0
        for i in range(1, len(points)):
            dist = points[i][0] - points[i-1][0]

            if dist > max_length:
                max_length = dist

        return max_length




            


        