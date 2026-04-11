class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0

        for i , h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                inx, height = stack.pop()
                max_area = max(max_area, height * (i - inx))
                start = inx

            stack.append((start, h))

        
        for inx, h in stack:
            max_area = max(max_area, h * (len(heights) - inx))
        
        return max_area
