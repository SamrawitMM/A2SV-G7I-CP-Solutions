class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        area = 0
        while left < right:
            min_height = min(height[left], height[right])
            a = min_height * (right -left)
            area = max(area, a)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return area
